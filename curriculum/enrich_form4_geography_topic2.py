"""
VLearn Form 4 Geography — Topic 2: Fishing
Visual Enrichment Engine (16 High-Precision Vector SVGs & 6 Verified Wikimedia Photographic Assets)

Topic: Fishing (Topic ID: 56)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)

Visual Inventory:
  Lesson 1:
    - SVG 1: Continental Shelf & Photic Zone Cross-Section
    - SVG 2: Ocean Current Convergence & Nutrient Upwelling Mechanism
    - Wikimedia 1: Glaciated Fiord Coastline in Norway Providing Natural Sheltered Inlets
  Lesson 2:
    - SVG 3: The Four Types of Fishing Taxonomy Tree & Depth Profile
    - SVG 4: Mechanics of Traditional Basket Trap and Gill Netting
    - Wikimedia 2: Traditional Wooden Dhows on the Coastal Waters of Kenya
  Lesson 3:
    - SVG 5: Operational Mechanics of Purse Seining (Surface Pelagic)
    - SVG 6: Bottom Trawling Operations and Benthic Habitat Disruption
    - Wikimedia 3: Commercial Trawler Winching Up a Heavy Marine Net
  Lesson 4:
    - SVG 7: Global Thematic Map of Major World Fishing Grounds & Ocean Currents
    - SVG 8: Spatial Map of the Northwest Atlantic & Grand Bank Current Convergence
    - SVG 9: Spatial Map of the Northwest Pacific Ground & Kuroshiwo/Oyashiwo Convergence
    - Wikimedia 4: Coho Salmon Spawning Run in the Pacific Northwest Rushing Rivers
  Lesson 5:
    - SVG 10: Profile of the Kenyan Marine Coastline (Narrow Shelf vs Indian Ocean)
    - SVG 11: Spatial Map of Inland Freshwater Fisheries and Hatcheries in Kenya
    - SVG 12: Lake Victoria Basin, Catchment, and Major Landing Beaches
    - SVG 13: Ecological Food Web Disruption & Invasive Hyacinth in Lake Victoria
    - SVG 14: Engineering Cross-Section of an Aquaculture Fish Pond and Water Flow
    - Wikimedia 5: Artisanal Wooden Fishing Boats and Operations on Lake Victoria in Kisumu
  Lesson 6:
    - SVG 15: Kenya vs Japan Fishing Technology and Oceanographic Setting Contrast
    - SVG 16: The Seven Core Strategies for Sustainable Fisheries Conservation
    - Wikimedia 6: Commercial Tuna Auction and Processing at Tsukiji Fish Market in Japan

Usage:
  ./venv/bin/python curriculum/enrich_form4_geography_topic2.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

BG = "#0a0f1d"
PANEL_BG = "#111827"
PANEL_BG_2 = "#1e293b"
BORDER_COLOR = "#334155"
TEXT_MAIN = "#f8fafc"
TEXT_MUTED = "#94a3b8"
ACCENT_BLUE = "#38bdf8"
ACCENT_GREEN = "#22c55e"
ACCENT_RED = "#ef4444"
ACCENT_AMBER = "#f59e0b"
ACCENT_PURPLE = "#a855f7"
ACCENT_TEAL = "#14b8a6"

def clean_svg(svg_code: str) -> str:
    is_valid, sanitized, err = validate_and_sanitize_svg(svg_code)
    if is_valid:
        return sanitized
    print(f"  [Warning] SVG Sanitization issue: {err}")
    return svg_code

def wrap_svg(inner_content, W=840, H=440, title=""):
    title_svg = ""
    if title:
        title_svg = (
            f'<rect x="0" y="0" width="{W}" height="48" fill="{PANEL_BG}" rx="16"/>'
            f'<text x="{W//2}" y="30" fill="{TEXT_MAIN}" font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="15" font-weight="700" text-anchor="middle" letter-spacing="0.5">{title}</text>'
            f'<line x1="0" y1="48" x2="{W}" y2="48" stroke="{BORDER_COLOR}" stroke-width="1"/>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">'
        f'<rect width="{W}" height="{H}" fill="{BG}" rx="16"/>'
        f'{title_svg}'
        f'{inner_content}'
        f'</svg>'
    )

def attach_svg_to_block(lesson, exact_diagram_title, builder_fn):
    svg_code = builder_fn()
    sanitized = clean_svg(svg_code)

    block = LessonBlock.objects.filter(
        lesson=lesson,
        block_type="suggested_diagram",
        title__icontains=exact_diagram_title
    ).first()

    if not block:
        block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_diagram",
            page_title__icontains=exact_diagram_title
        ).first()

    if not block:
        candidates = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").order_by("order")
        for cand in candidates:
            if not cand.content.get("svg_content") and not cand.content.get("svg"):
                block = cand
                break

    if not block:
        last_block = lesson.blocks.order_by("-order").first()
        last_order = (last_block.order if last_block else 0) + 10
        last_page = (last_block.page_number if last_block else 0) + 1
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=last_page,
            page_title=f"Diagram: {exact_diagram_title}",
            title=exact_diagram_title,
            block_type="suggested_diagram",
            component_type="suggested_diagram",
            component_order=last_order,
            order=last_order,
            content={}
        )

    block.title = exact_diagram_title
    block.block_type = "suggested_diagram"
    block.component_type = "suggested_diagram"
    if not block.metadata:
        block.metadata = {}
    block.metadata["svg_content"] = sanitized

    if not isinstance(block.content, dict):
        block.content = {}
    block.content["svg_content"] = sanitized
    block.content["svg"] = sanitized
    block.content["title"] = exact_diagram_title
    block.content["text"] = f"Vector diagram illustration: {exact_diagram_title}"
    block.save()

    asset = LessonAsset.objects.create(
        lesson=lesson,
        asset_type="diagram",
        source_type="ai_generated",
        storage_type="embed",
        status="attached",
        title=exact_diagram_title,
        description=f"Sanitized vector diagram: {exact_diagram_title}",
        metadata={"svg_content": sanitized}
    )
    block.assets.add(asset)

    print(f"  [SVG OK] '{exact_diagram_title[:45]}' -> Block ID: {block.id} (Page {block.page_number})")
    return asset

def attach_wikimedia_to_block(lesson, exact_title, verified_url, author, licensing, commons_page):
    block = LessonBlock.objects.filter(
        lesson=lesson,
        block_type="suggested_image",
        title__icontains=exact_title
    ).first()

    if not block:
        candidates = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_image").order_by("order")
        for cand in candidates:
            if not cand.content.get("resolved_image_url") and not cand.content.get("url"):
                block = cand
                break

    if not block:
        last_block = lesson.blocks.order_by("-order").first()
        last_order = (last_block.order if last_block else 0) + 10
        last_page = (last_block.page_number if last_block else 0) + 1
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=last_page,
            page_title=f"Photographic Asset — {exact_title}",
            title=exact_title,
            block_type="suggested_image",
            component_type="suggested_image",
            component_order=last_order,
            order=last_order,
            content={}
        )

    block.title = exact_title
    block.block_type = "suggested_image"
    block.component_type = "suggested_image"
    if not isinstance(block.content, dict):
        block.content = {}
    block.content["title"] = exact_title
    block.content["url"] = verified_url
    block.content["resolved_image_url"] = verified_url
    block.content["author"] = author
    block.content["licensing"] = licensing
    block.content["commons_page_url"] = commons_page
    block.save()

    asset = LessonAsset.objects.create(
        lesson=lesson,
        asset_type="image",
        source_type="external",
        storage_type="url",
        status="attached",
        title=exact_title,
        description=f"Wikimedia Commons photographic asset: {exact_title}",
        url=verified_url,
        metadata={
            "author": author,
            "licensing": licensing,
            "commons_page_url": commons_page,
        }
    )
    block.assets.add(asset)

    print(f"  [WIKIMEDIA OK] '{exact_title[:45]}' -> Block ID: {block.id} (Page {block.page_number})")
    return asset


# =============================================================================
# 16 HIGH-PRECISION SVG BUILDERS FOR TOPIC 2
# =============================================================================

def svg_photic_zone_continental_shelf():
    """SVG 1: Continental Shelf & Photic Zone Cross-Section"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Land / Coastline on Left -->
      <path d="M 0,80 L 80,80 L 120,130 L 120,330 L 0,330 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="50" y="150" fill="{TEXT_MAIN}" font-size="12" font-weight="700" text-anchor="middle">Coast / Land</text>

      <!-- Photic Zone Water (0 - 180m) in Bright Blue -->
      <polygon points="120,130 500,160 500,210 120,210" fill="{ACCENT_BLUE}33" stroke="{ACCENT_BLUE}" stroke-width="1.5"/>
      <text x="310" y="150" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">Sunlit Photic Zone (0 – 180 m Depth)</text>
      
      <!-- Sunlight Rays Penetrating -->
      <line x1="200" y1="90" x2="220" y2="180" stroke="{ACCENT_AMBER}" stroke-width="2" stroke-dasharray="3,3"/>
      <line x1="300" y1="90" x2="320" y2="180" stroke="{ACCENT_AMBER}" stroke-width="2" stroke-dasharray="3,3"/>
      <line x1="400" y1="90" x2="420" y2="180" stroke="{ACCENT_AMBER}" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="310" y="105" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">Solar Radiation Penetration</text>

      <!-- Plankton Blooms in Green -->
      <circle cx="220" cy="165" r="5" fill="{ACCENT_GREEN}"/>
      <circle cx="250" cy="175" r="4" fill="{ACCENT_GREEN}"/>
      <circle cx="340" cy="168" r="6" fill="{ACCENT_GREEN}"/>
      <circle cx="410" cy="172" r="5" fill="{ACCENT_GREEN}"/>
      <text x="310" y="195" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">Phytoplankton &amp; Zooplankton Proliferation</text>

      <!-- Continental Shelf Seabed -->
      <path d="M 120,210 L 500,210 L 650,330 L 760,330 L 760,350 L 120,350 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="310" y="240" fill="{TEXT_MAIN}" font-size="12" font-weight="700" text-anchor="middle">Broad Continental Shelf (Shallow Waters)</text>

      <!-- Continental Slope & Deep Sea Abyss -->
      <text x="590" y="265" fill="{TEXT_MUTED}" font-size="11" transform="rotate(38, 590, 265)">Continental Slope</text>
      <text x="700" y="315" fill="{TEXT_MUTED}" font-size="11" text-anchor="middle">Deep Ocean Floor (>2,000m)</text>
      <text x="700" y="330" fill="{ACCENT_RED}" font-size="10" text-anchor="middle">(Dark Aphotic Desert)</text>

      <!-- Fish Shoals -->
      <g fill="{ACCENT_BLUE}">
        <ellipse cx="280" cy="170" rx="8" ry="3"/>
        <ellipse cx="300" cy="165" rx="7" ry="3"/>
        <ellipse cx="380" cy="175" rx="8" ry="4"/>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Continental Shelf & Photic Zone Dynamics for Plankton Proliferation")

def svg_current_convergence_upwelling():
    """SVG 2: Ocean Current Convergence & Nutrient Upwelling Mechanism"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Sea Surface & Seabed -->
      <rect x="0" y="50" width="760" height="20" fill="{ACCENT_BLUE}22"/>
      <line x1="0" y1="50" x2="760" y2="50" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="380" y="40" fill="{ACCENT_BLUE}" font-size="12" font-weight="700" text-anchor="middle">Sea Surface Level</text>

      <rect x="0" y="280" width="760" height="50" fill="{PANEL_BG_2}"/>
      <line x1="0" y1="280" x2="760" y2="280" stroke="{BORDER_COLOR}" stroke-width="2"/>
      <text x="380" y="310" fill="{TEXT_MUTED}" font-size="12" font-weight="700" text-anchor="middle">Deep Ocean Seabed (Mineral Nutrients &amp; Organic Sediments)</text>

      <!-- Left: Warm Current -->
      <path d="M 60,70 L 320,70 Q 370,70 370,120 L 370,220" fill="none" stroke="{ACCENT_AMBER}" stroke-width="6"/>
      <text x="180" y="95" fill="{ACCENT_AMBER}" font-size="13" font-weight="700">Warm Ocean Current (Surface Flow)</text>
      <text x="180" y="115" fill="{TEXT_MUTED}" font-size="10">e.g., Gulf Stream / Kuroshiwo</text>

      <!-- Right: Cold Dense Current -->
      <path d="M 700,80 L 440,80 Q 390,80 390,160 L 390,260" fill="none" stroke="{ACCENT_BLUE}" stroke-width="6"/>
      <text x="580" y="95" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">Cold Dense Current</text>
      <text x="580" y="115" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">e.g., Labrador / Oyashiwo</text>

      <!-- Central Upwelling Convective Zone -->
      <g transform="translate(320, 130)">
        <rect width="120" height="140" fill="{PANEL_BG}" rx="8" stroke="{ACCENT_GREEN}" stroke-width="2"/>
        <!-- Upwelling Arrows -->
        <line x1="60" y1="130" x2="60" y2="20" stroke="{ACCENT_GREEN}" stroke-width="4"/>
        <polygon points="50,30 60,10 70,30" fill="{ACCENT_GREEN}"/>
        <text x="60" y="70" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">VERTICAL</text>
        <text x="60" y="85" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">UPWELLING</text>
        <text x="60" y="105" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Nutrient Lift</text>
      </g>

      <!-- Plankton Bloom at Surface Convergence -->
      <ellipse cx="380" cy="50" rx="90" ry="18" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="380" y="55" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">Dense Plankton Bloom</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Ocean Current Convergence, Vertical Upwelling, and Nutrient Cycling")

def svg_four_fishery_types():
    """SVG 3: The Four Types of Fishing Taxonomy Tree & Depth Profile"""
    inner = f"""
    <!-- Root Node -->
    <g transform="translate(260, 60)">
      <rect width="320" height="45" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="160" y="28" fill="{TEXT_MAIN}" font-size="14" font-weight="700" text-anchor="middle">THE FOUR TYPES OF FISHING</text>
    </g>

    <!-- Branch Lines -->
    <line x1="420" y1="105" x2="420" y2="125" stroke="{BORDER_COLOR}" stroke-width="2"/>
    <line x1="120" y1="125" x2="720" y2="125" stroke="{BORDER_COLOR}" stroke-width="2"/>
    <line x1="120" y1="125" x2="120" y2="145" stroke="{ACCENT_BLUE}" stroke-width="2"/>
    <line x1="320" y1="125" x2="320" y2="145" stroke="{ACCENT_PURPLE}" stroke-width="2"/>
    <line x1="520" y1="125" x2="520" y2="145" stroke="{ACCENT_AMBER}" stroke-width="2"/>
    <line x1="720" y1="125" x2="720" y2="145" stroke="{ACCENT_GREEN}" stroke-width="2"/>

    <!-- 4 Category Cards -->
    <!-- 1. Pelagic -->
    <g transform="translate(30, 145)">
      <rect width="180" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="90" y="28" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">1. PELAGIC</text>
      <text x="90" y="50" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Surface Open Waters</text>
      <text x="15" y="80" fill="{TEXT_MUTED}" font-size="10">• Depth: Upper 0–200m</text>
      <text x="15" y="100" fill="{TEXT_MUTED}" font-size="10">• Behavior: Dense shoals</text>
      <text x="15" y="130" fill="{ACCENT_BLUE}" font-size="11" font-weight="600">Key Species:</text>
      <text x="15" y="150" fill="{TEXT_MAIN}" font-size="10">Tuna, Mackerel, Herring, Sardines</text>
      <text x="15" y="180" fill="{ACCENT_BLUE}" font-size="11" font-weight="600">Dominant Gear:</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">Purse Seine, Drift Net</text>
    </g>

    <!-- 2. Demersal -->
    <g transform="translate(230, 145)">
      <rect width="180" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}" stroke-width="2"/>
      <text x="90" y="28" fill="{ACCENT_PURPLE}" font-size="13" font-weight="700" text-anchor="middle">2. DEMERSAL</text>
      <text x="90" y="50" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Ocean Floor / Benthic</text>
      <text x="15" y="80" fill="{TEXT_MUTED}" font-size="10">• Depth: Deep seabed</text>
      <text x="15" y="100" fill="{TEXT_MUTED}" font-size="10">• Behavior: Bottom feeding</text>
      <text x="15" y="130" fill="{ACCENT_PURPLE}" font-size="11" font-weight="600">Key Species:</text>
      <text x="15" y="150" fill="{TEXT_MAIN}" font-size="10">Cod, Haddock, Halibut, Pollock</text>
      <text x="15" y="180" fill="{ACCENT_PURPLE}" font-size="11" font-weight="600">Dominant Gear:</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">Bottom Trawl, Long Line</text>
    </g>

    <!-- 3. Inshore -->
    <g transform="translate(430, 145)">
      <rect width="180" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <text x="90" y="28" fill="{ACCENT_AMBER}" font-size="13" font-weight="700" text-anchor="middle">3. INSHORE</text>
      <text x="90" y="50" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Coastlines &amp; Estuaries</text>
      <text x="15" y="80" fill="{TEXT_MUTED}" font-size="10">• Depth: Shallow bays</text>
      <text x="15" y="100" fill="{TEXT_MUTED}" font-size="10">• Environment: Mangroves</text>
      <text x="15" y="130" fill="{ACCENT_AMBER}" font-size="11" font-weight="600">Key Species:</text>
      <text x="15" y="150" fill="{TEXT_MAIN}" font-size="10">Prawns, Crabs, Lobsters, Shellfish</text>
      <text x="15" y="180" fill="{ACCENT_AMBER}" font-size="11" font-weight="600">Dominant Gear:</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">Cast Nets, Traps, Lines</text>
    </g>

    <!-- 4. Freshwater -->
    <g transform="translate(630, 145)">
      <rect width="180" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="90" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">4. FRESHWATER</text>
      <text x="90" y="50" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Inland Lakes &amp; Rivers</text>
      <text x="15" y="80" fill="{TEXT_MUTED}" font-size="10">• Depth: Calm shallows</text>
      <text x="15" y="100" fill="{TEXT_MUTED}" font-size="10">• Environment: Non-saline</text>
      <text x="15" y="130" fill="{ACCENT_GREEN}" font-size="11" font-weight="600">Key Species:</text>
      <text x="15" y="150" fill="{TEXT_MAIN}" font-size="10">Tilapia, Nile Perch, Trout, Dagaa</text>
      <text x="15" y="180" fill="{ACCENT_GREEN}" font-size="11" font-weight="600">Dominant Gear:</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">Gill Net, Hook &amp; Line</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Ecological Classification and Gear Zonation of Global Fisheries")

def svg_basket_and_gillnet():
    """SVG 4: Mechanics of Traditional Basket Trap and Gill Netting"""
    inner = f"""
    <!-- Left: Traditional Woven Basket Trap -->
    <g transform="translate(30, 65)">
      <rect width="360" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="180" y="28" fill="{ACCENT_AMBER}" font-size="13" font-weight="700" text-anchor="middle">1. Woven Conical Basket Trap</text>
      
      <!-- Basket Cone Schematic -->
      <polygon points="60,110 300,70 300,250 60,210" fill="{PANEL_BG_2}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <!-- Non-Return Inverted Funnel Entrance -->
      <polygon points="60,110 160,140 160,180 60,210" fill="{BG}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <!-- Bait in rear -->
      <circle cx="260" cy="160" r="15" fill="{ACCENT_RED}44" stroke="{ACCENT_RED}"/>
      <text x="260" y="164" fill="{ACCENT_RED}" font-size="9" font-weight="700" text-anchor="middle">Bait</text>
      
      <!-- Fish Entry Vector -->
      <path d="M 20,160 L 120,160" stroke="{ACCENT_BLUE}" stroke-width="3" stroke-dasharray="3,3"/>
      <polygon points="120,155 135,160 120,165" fill="{ACCENT_BLUE}"/>
      <text x="180" y="290" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Non-Return Funnel Entrance</text>
      <text x="180" y="310" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Fish swim in towards bait but cannot locate narrow escape point</text>
    </g>

    <!-- Right: Gill Net Operculum Action -->
    <g transform="translate(420, 65)">
      <rect width="390" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="195" y="28" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">2. Gill Net Operculum Trapping Action</text>

      <!-- Float line & weights -->
      <line x1="40" y1="60" x2="350" y2="60" stroke="{ACCENT_BLUE}" stroke-width="4"/>
      <circle cx="90" cy="60" r="6" fill="{ACCENT_AMBER}"/>
      <circle cx="195" cy="60" r="6" fill="{ACCENT_AMBER}"/>
      <circle cx="300" cy="60" r="6" fill="{ACCENT_AMBER}"/>
      <text x="195" y="50" fill="{ACCENT_AMBER}" font-size="9" text-anchor="middle">Surface Floats</text>

      <!-- Vertical Mesh Grid -->
      <g stroke="{BORDER_COLOR}" stroke-width="1.5">
        <line x1="80" y1="60" x2="80" y2="250"/>
        <line x1="140" y1="60" x2="140" y2="250"/>
        <line x1="200" y1="60" x2="200" y2="250"/>
        <line x1="260" y1="60" x2="260" y2="250"/>
        <line x1="320" y1="60" x2="320" y2="250"/>
        <line x1="40" y1="110" x2="350" y2="110"/>
        <line x1="40" y1="160" x2="350" y2="160"/>
        <line x1="40" y1="210" x2="350" y2="210"/>
      </g>

      <!-- Fish Trapped in Mesh by Operculum -->
      <ellipse cx="200" cy="160" rx="40" ry="14" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <line x1="200" y1="146" x2="200" y2="174" stroke="{ACCENT_RED}" stroke-width="3"/>
      <text x="200" y="195" fill="{ACCENT_RED}" font-size="10" font-weight="700" text-anchor="middle">Operculum (Gill Cover) Trapped</text>

      <text x="195" y="290" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Mesh Size Selectivity</text>
      <text x="195" y="310" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Head passes through; twine catches gills when fish attempts reverse</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Comparative Mechanics of Traditional Basket Traps and Gill Netting")

def svg_purse_seining():
    """SVG 5: Operational Mechanics of Purse Seining (Surface Pelagic)"""
    inner = f"""
    <!-- 4 Stage Sequential Process -->
    <g transform="translate(30, 65)">
      <!-- Stage 1 -->
      <g transform="translate(0, 0)">
        <rect width="180" height="340" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="90" y="25" fill="{ACCENT_BLUE}" font-size="12" font-weight="700" text-anchor="middle">Stage 1: Sonar Detection</text>
        <rect x="20" y="50" width="140" height="70" fill="{PANEL_BG_2}" rx="6"/>
        <ellipse cx="90" cy="85" rx="30" ry="12" fill="{ACCENT_GREEN}55"/>
        <text x="90" y="90" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Surface Shoal</text>
        <text x="90" y="150" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Sonar / spotter helicopter</text>
        <text x="90" y="170" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">locates massive school</text>
        <text x="90" y="190" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">of pelagic fish (Tuna).</text>
      </g>

      <!-- Stage 2 -->
      <g transform="translate(200, 0)">
        <rect width="180" height="340" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="90" y="25" fill="{ACCENT_AMBER}" font-size="12" font-weight="700" text-anchor="middle">Stage 2: Encirclement</text>
        <rect x="20" y="50" width="140" height="70" fill="{PANEL_BG_2}" rx="6"/>
        <circle cx="90" cy="85" r="25" fill="none" stroke="{ACCENT_AMBER}" stroke-width="2.5" stroke-dasharray="4,4"/>
        <text x="90" y="150" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Skiff boat deploys net</text>
        <text x="90" y="170" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">in a wide circular wall</text>
        <text x="90" y="190" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">around the fish shoal.</text>
      </g>

      <!-- Stage 3 -->
      <g transform="translate(400, 0)">
        <rect width="180" height="340" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="90" y="25" fill="{ACCENT_RED}" font-size="12" font-weight="700" text-anchor="middle">Stage 3: Pursing Net</text>
        <rect x="20" y="50" width="140" height="70" fill="{PANEL_BG_2}" rx="6"/>
        <path d="M 50,65 Q 90,110 130,65" fill="{ACCENT_BLUE}33" stroke="{ACCENT_RED}" stroke-width="3"/>
        <text x="90" y="150" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Bottom purse wire</text>
        <text x="90" y="170" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">winched tight like a</text>
        <text x="90" y="190" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">drawstring purse.</text>
      </g>

      <!-- Stage 4 -->
      <g transform="translate(600, 0)">
        <rect width="180" height="340" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="90" y="25" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">Stage 4: Vacuum Pumping</text>
        <rect x="20" y="50" width="140" height="70" fill="{PANEL_BG_2}" rx="6"/>
        <rect x="50" y="65" width="80" height="40" fill="{ACCENT_GREEN}44" rx="4"/>
        <text x="90" y="90" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Refrigerated Hold</text>
        <text x="90" y="150" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Hydraulic suction pipe</text>
        <text x="90" y="170" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">pumps catch directly</text>
        <text x="90" y="190" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">into freezing tanks.</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Operational Mechanics of Purse Seining (Surface Pelagic Fisheries)")

def svg_bottom_trawling():
    """SVG 6: Bottom Trawling Operations and Benthic Habitat Disruption"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Sea Surface & Trawler Ship -->
      <line x1="20" y1="40" x2="740" y2="40" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <polygon points="60,40 160,40 140,10 80,10" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="110" y="30" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">Trawler Vessel</text>

      <!-- Steel Tow Warps -->
      <line x1="140" y1="40" x2="380" y2="200" stroke="{TEXT_MUTED}" stroke-width="2.5"/>
      <text x="240" y="110" fill="{TEXT_MUTED}" font-size="10" transform="rotate(30, 240, 110)">Steel Tow Cables</text>

      <!-- Otter Boards (Trawl Doors) -->
      <rect x="370" y="190" width="20" height="45" fill="{ACCENT_RED}" rx="3"/>
      <text x="380" y="180" fill="{ACCENT_RED}" font-size="10" font-weight="700" text-anchor="middle">Otter Board</text>

      <!-- Funnel Net & Cod-End -->
      <polygon points="380,210 580,240 580,275 380,245" fill="{ACCENT_BLUE}33" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <rect x="580" y="242" width="60" height="30" fill="{ACCENT_PURPLE}44" stroke="{ACCENT_PURPLE}" stroke-width="2" rx="4"/>
      <text x="610" y="260" fill="{ACCENT_PURPLE}" font-size="10" font-weight="700" text-anchor="middle">Cod-End</text>

      <!-- Weighted Footrope on Seabed -->
      <line x1="380" y1="245" x2="580" y2="275" stroke="{ACCENT_AMBER}" stroke-width="4"/>
      <text x="480" y="240" fill="{ACCENT_AMBER}" font-size="9" text-anchor="middle">Weighted Steel Bobbins</text>

      <!-- Seabed Destruction Zone -->
      <rect x="20" y="275" width="720" height="55" fill="{PANEL_BG_2}"/>
      <line x1="20" y1="275" x2="740" y2="275" stroke="{ACCENT_RED}" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="480" y="300" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">Seabed Scouring: Destruction of Coral Reefs &amp; Benthic Habitats</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Bottom Trawling Operations and Benthic Seabed Disruption")

def svg_world_fishing_grounds():
    """SVG 7: Global Thematic Map of Major World Fishing Grounds & Ocean Currents"""
    inner = f"""
    <!-- World Map Canvas -->
    <g transform="translate(40, 65)">
      <!-- Continents simplified representation -->
      <!-- North America -->
      <polygon points="40,60 180,40 220,110 160,180 80,140 40,90" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="110" y="110" fill="{TEXT_MUTED}" font-size="12" font-weight="700">North America</text>

      <!-- Europe -->
      <polygon points="340,40 450,40 440,110 360,110" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="390" y="80" fill="{TEXT_MUTED}" font-size="11" font-weight="700">Europe</text>

      <!-- Asia -->
      <polygon points="470,30 680,40 680,160 540,180 480,120" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="580" y="90" fill="{TEXT_MUTED}" font-size="12" font-weight="700">Asia</text>

      <!-- Africa -->
      <polygon points="340,130 440,130 420,260 360,260" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="385" y="190" fill="{TEXT_MUTED}" font-size="11" font-weight="700">Africa</text>

      <!-- South America -->
      <polygon points="140,190 220,190 180,310 120,250" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="170" y="240" fill="{TEXT_MUTED}" font-size="10" font-weight="700">S. America</text>

      <!-- 4 MAJOR NORTHERN FISHING GROUNDS (Green Highlight) -->
      <!-- 1. NW Atlantic (Grand Bank) -->
      <ellipse cx="230" cy="80" rx="35" ry="25" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="230" y="78" fill="{TEXT_MAIN}" font-size="9" font-weight="700" text-anchor="middle">1. NW Atlantic</text>
      <text x="230" y="90" fill="{TEXT_MAIN}" font-size="8" text-anchor="middle">(Grand Bank)</text>

      <!-- 2. NE Atlantic (Western Europe) -->
      <ellipse cx="340" cy="65" rx="35" ry="25" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="340" y="65" fill="{TEXT_MAIN}" font-size="9" font-weight="700" text-anchor="middle">2. NE Atlantic</text>
      <text x="340" y="77" fill="{TEXT_MAIN}" font-size="8" text-anchor="middle">(North Sea/Norway)</text>

      <!-- 3. NW Pacific (Japan/East Asia) -->
      <ellipse cx="690" cy="90" rx="40" ry="30" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="690" y="88" fill="{TEXT_MAIN}" font-size="9" font-weight="700" text-anchor="middle">3. NW Pacific</text>
      <text x="690" y="100" fill="{TEXT_MAIN}" font-size="8" text-anchor="middle">(Japan / China)</text>

      <!-- 4. NE Pacific (Alaska/BC) -->
      <ellipse cx="40" cy="65" rx="35" ry="25" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="40" y="65" fill="{TEXT_MAIN}" font-size="9" font-weight="700" text-anchor="middle">4. NE Pacific</text>
      <text x="40" y="77" fill="{TEXT_MAIN}" font-size="8" text-anchor="middle">(Salmon)</text>

      <!-- Southern Upwelling Grounds (Amber Highlight) -->
      <!-- Peru -->
      <circle cx="115" cy="230" r="14" fill="{ACCENT_AMBER}66" stroke="{ACCENT_AMBER}"/>
      <text x="115" y="255" fill="{ACCENT_AMBER}" font-size="8" text-anchor="middle">Peru (Humboldt)</text>

      <!-- Benguela (SW Africa) -->
      <circle cx="360" cy="260" r="14" fill="{ACCENT_AMBER}66" stroke="{ACCENT_AMBER}"/>
      <text x="360" y="285" fill="{ACCENT_AMBER}" font-size="8" text-anchor="middle">Benguela (Namibia)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Global Distribution of the Major Marine Fishing Grounds & Upwelling Zones")

def svg_nw_atlantic_grand_bank():
    """SVG 8: Spatial Map of the Northwest Atlantic & Grand Bank Current Convergence"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- North America Coastline -->
      <path d="M 20,40 L 140,40 L 220,120 L 180,240 L 100,320 L 20,320 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="90" y="160" fill="{TEXT_MAIN}" font-size="13" font-weight="700">Eastern Canada &amp; USA</text>
      <text x="90" y="180" fill="{TEXT_MUTED}" font-size="10">(Newfoundland &amp; Nova Scotia)</text>

      <!-- Grand Bank Shallow Zone -->
      <ellipse cx="440" cy="180" rx="140" ry="90" fill="{ACCENT_GREEN}33" stroke="{ACCENT_GREEN}" stroke-width="2.5"/>
      <text x="440" y="175" fill="{ACCENT_GREEN}" font-size="16" font-weight="700" text-anchor="middle">GRAND BANK</text>
      <text x="440" y="195" fill="{TEXT_MAIN}" font-size="11" text-anchor="middle">Extensive Shallow Continental Shelf (&lt;180m)</text>

      <!-- Cold Labrador Current (Flowing South) -->
      <path d="M 440,40 L 440,120" stroke="{ACCENT_BLUE}" stroke-width="5"/>
      <polygon points="430,110 440,135 450,110" fill="{ACCENT_BLUE}"/>
      <text x="460" y="70" fill="{ACCENT_BLUE}" font-size="12" font-weight="700">Cold Labrador Current</text>

      <!-- Warm Gulf Stream (Flowing North-East) -->
      <path d="M 240,290 L 380,230" stroke="{ACCENT_AMBER}" stroke-width="5"/>
      <polygon points="370,245 395,225 385,215" fill="{ACCENT_AMBER}"/>
      <text x="240" y="275" fill="{ACCENT_AMBER}" font-size="12" font-weight="700">Warm Gulf Stream</text>

      <!-- Collision / Nutrient Upwelling Zone -->
      <ellipse cx="410" cy="190" rx="50" ry="30" fill="{ACCENT_TEAL}44" stroke="{ACCENT_TEAL}" stroke-dasharray="3,3"/>
      <text x="410" y="215" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Upwelling Convergence</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="The Northwest Atlantic Grounds: Grand Bank & Current Convergence")

def svg_nw_pacific_japan():
    """SVG 9: Spatial Map of the Northwest Pacific Ground & Kuroshiwo/Oyashiwo Convergence"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Asian Mainland Coastline (Left) -->
      <path d="M 20,40 L 160,40 L 140,320 L 20,320 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="70" y="160" fill="{TEXT_MUTED}" font-size="12" font-weight="700">Asian Mainland</text>

      <!-- Japanese Archipelago Islands -->
      <!-- Hokkaido -->
      <polygon points="340,60 420,50 400,100 330,90" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="370" y="80" fill="{TEXT_MAIN}" font-size="10" font-weight="700">Hokkaido</text>

      <!-- Honshu -->
      <path d="M 330,110 Q 380,180 280,260 L 260,250 Q 340,170 310,110 Z" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="340" y="190" fill="{TEXT_MAIN}" font-size="12" font-weight="700">Honshu (Japan)</text>

      <!-- Sea of Japan -->
      <text x="210" y="150" fill="{ACCENT_BLUE}" font-size="11" font-weight="700">Sea of Japan</text>

      <!-- Cold Oyashiwo Current (South from Bering Sea) -->
      <path d="M 520,40 L 460,110" stroke="{ACCENT_BLUE}" stroke-width="5"/>
      <polygon points="460,95 445,120 470,110" fill="{ACCENT_BLUE}"/>
      <text x="540" y="65" fill="{ACCENT_BLUE}" font-size="12" font-weight="700">Cold Oyashiwo Current</text>

      <!-- Warm Kuroshiwo Current (North from Equator) -->
      <path d="M 380,310 L 440,210" stroke="{ACCENT_AMBER}" stroke-width="5"/>
      <polygon points="430,225 450,195 450,220" fill="{ACCENT_AMBER}"/>
      <text x="470" y="270" fill="{ACCENT_AMBER}" font-size="12" font-weight="700">Warm Kuroshiwo Current</text>

      <!-- Convergence Zone Highlight -->
      <ellipse cx="460" cy="150" rx="70" ry="45" fill="{ACCENT_GREEN}33" stroke="{ACCENT_GREEN}" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="460" y="145" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">RICHEST PLANKTON HAVEN</text>
      <text x="460" y="162" fill="{ACCENT_GREEN}" font-size="10" text-anchor="middle">(World's #1 Fishery Output)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="The Northwest Pacific Grounds: Japan and Kuroshiwo/Oyashiwo Meeting")

def svg_kenya_marine_profile():
    """SVG 10: Profile of the Kenyan Marine Coastline (Narrow Shelf vs Indian Ocean)"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Kenya Coastline Land Profile -->
      <path d="M 20,80 L 140,80 L 180,160 L 260,180 L 320,330 L 20,330 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="90" y="140" fill="{TEXT_MAIN}" font-size="13" font-weight="700">Kenya Coast</text>
      <text x="90" y="160" fill="{TEXT_MUTED}" font-size="10">(Mombasa / Malindi)</text>

      <!-- Fringing Coral Reef -->
      <polygon points="200,165 220,150 240,165" fill="{ACCENT_AMBER}" stroke="{BORDER_COLOR}"/>
      <text x="220" y="140" fill="{ACCENT_AMBER}" font-size="9" font-weight="700" text-anchor="middle">Coral Reef</text>

      <!-- Narrow Shelf (Very Short Distance) -->
      <line x1="180" y1="195" x2="260" y2="195" stroke="{ACCENT_RED}" stroke-width="3"/>
      <text x="220" y="215" fill="{ACCENT_RED}" font-size="10" font-weight="700" text-anchor="middle">Narrow Shelf (<15km)</text>

      <!-- Steep Drop-off into Deep Indian Ocean -->
      <path d="M 260,180 Q 290,260 380,330 L 740,330 L 740,120 L 180,120 Z" fill="{ACCENT_BLUE}22"/>
      <line x1="180" y1="120" x2="740" y2="120" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="480" y="105" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">Indian Ocean Waters</text>

      <!-- Warm Mozambique Current -->
      <path d="M 380,140 L 640,140" stroke="{ACCENT_AMBER}" stroke-width="4"/>
      <text x="510" y="160" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">Warm Mozambique Current (Low Plankton)</text>

      <!-- Deep-Sea Foreign Trawler Zone -->
      <rect x="480" y="220" width="220" height="70" rx="6" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="590" y="245" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Deep EEZ Waters</text>
      <text x="590" y="265" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Dominated by foreign commercial trawlers</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Topographic Profile of the Kenyan Marine Coastline & Physical Bottlenecks")

def svg_kenya_inland_fisheries_map():
    """SVG 11: Spatial Map of Inland Freshwater Fisheries and Hatcheries in Kenya"""
    inner = f"""
    <!-- Kenya Map Outline -->
    <g transform="translate(40, 60)">
      <!-- Country Polygon -->
      <path d="M 120,30 L 220,20 L 290,80 L 320,160 L 300,270 L 250,320 L 190,310 L 130,280 L 100,230 L 80,170 L 70,100 Z"
            fill="{PANEL_BG}" stroke="{BORDER_COLOR}" stroke-width="2"/>

      <!-- Lake Victoria (Powerhouse) -->
      <ellipse cx="65" cy="190" rx="25" ry="35" fill="{ACCENT_BLUE}66" stroke="{ACCENT_BLUE}" stroke-width="2.5"/>
      <text x="65" y="195" fill="{TEXT_MAIN}" font-size="10" font-weight="700" text-anchor="middle">L. Victoria</text>
      <text x="65" y="240" fill="{ACCENT_GREEN}" font-size="9" font-weight="700" text-anchor="middle">(90% Catch)</text>

      <!-- Lake Turkana (Alkaline Commercial Lake) -->
      <path d="M 120,40 L 135,110 L 115,110 Z" fill="{ACCENT_BLUE}55" stroke="{ACCENT_BLUE}" stroke-width="1.5"/>
      <text x="140" y="75" fill="{ACCENT_BLUE}" font-size="10" font-weight="700">L. Turkana (Alkaline)</text>

      <!-- Lake Naivasha & Baringo -->
      <circle cx="135" cy="180" r="6" fill="{ACCENT_TEAL}"/>
      <text x="150" y="185" fill="{TEXT_MAIN}" font-size="9">L. Naivasha</text>

      <circle cx="130" cy="150" r="5" fill="{ACCENT_TEAL}"/>
      <text x="145" y="155" fill="{TEXT_MAIN}" font-size="9">L. Baringo</text>

      <!-- Government Hatcheries (Red Stars) -->
      <g fill="{ACCENT_RED}">
        <!-- Sagana -->
        <circle cx="180" cy="190" r="5"/>
        <!-- Kabaru -->
        <circle cx="170" cy="175" r="5"/>
        <!-- Kibos -->
        <circle cx="95" cy="185" r="5"/>
        <!-- Aruba -->
        <circle cx="230" cy="280" r="5"/>
      </g>
    </g>

    <!-- Side Legend Panel -->
    <g transform="translate(420, 70)">
      <rect width="380" height="330" fill="{PANEL_BG}" rx="10" stroke="{BORDER_COLOR}"/>
      <text x="20" y="30" fill="{ACCENT_BLUE}" font-size="14" font-weight="700">Kenyan Fisheries Distribution</text>

      <text x="20" y="65" fill="{ACCENT_GREEN}" font-size="12" font-weight="700">1. Freshwater Powerhouse (Lake Victoria)</text>
      <text x="20" y="85" fill="{TEXT_MUTED}" font-size="10.5">• Produces >90% of national fish tonnage</text>
      <text x="20" y="103" fill="{TEXT_MUTED}" font-size="10.5">• Tilapia, Nile perch (export), Omena (diet/feed)</text>

      <text x="20" y="135" fill="{ACCENT_BLUE}" font-size="12" font-weight="700">2. Alkaline Commercial Exception</text>
      <text x="20" y="155" fill="{TEXT_MUTED}" font-size="10.5">• Lake Turkana: only commercial saline fishery</text>

      <text x="20" y="185" fill="{ACCENT_RED}" font-size="12" font-weight="700">3. Government Fish Hatcheries Network</text>
      <text x="20" y="205" fill="{TEXT_MAIN}" font-size="10">• Sagana (Kirinyaga): Warm-water Tilapia &amp; Catfish</text>
      <text x="20" y="223" fill="{TEXT_MAIN}" font-size="10">• Kabaru (Nyeri): Cold-water Trout</text>
      <text x="20" y="241" fill="{TEXT_MAIN}" font-size="10">• Kibos (Kisumu): Lake Basin fingerlings</text>
      <text x="20" y="259" fill="{TEXT_MAIN}" font-size="10">• Aruba (Taita Taveta): Coastal/Dryland ponds</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Spatial Map of Inland Freshwater Fisheries and Hatcheries in Kenya")

def svg_lake_victoria_basin():
    """SVG 12: Lake Victoria Basin, Catchment, and Major Landing Beaches"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Lake Victoria Polygon -->
      <path d="M 60,80 Q 180,40 300,90 Q 380,180 340,280 Q 200,330 80,260 Q 30,160 60,80 Z" fill="{ACCENT_BLUE}33" stroke="{ACCENT_BLUE}" stroke-width="2.5"/>
      <text x="200" y="170" fill="{ACCENT_BLUE}" font-size="16" font-weight="700" text-anchor="middle">LAKE VICTORIA</text>

      <!-- Kenyan Winam Gulf Sector (6%) -->
      <path d="M 280,100 Q 380,130 380,160 Q 340,190 290,170 Z" fill="{ACCENT_GREEN}44" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="350" y="145" fill="{TEXT_MAIN}" font-size="10" font-weight="700">Winam Gulf (Kenya 6%)</text>

      <!-- Key Landing Beaches -->
      <circle cx="370" cy="155" r="5" fill="{ACCENT_RED}"/>
      <text x="370" y="175" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Kisumu Port</text>

      <circle cx="330" cy="175" r="5" fill="{ACCENT_RED}"/>
      <text x="330" y="195" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Mbita Beach</text>

      <circle cx="310" cy="130" r="5" fill="{ACCENT_RED}"/>
      <text x="310" y="120" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">Asembo Bay</text>

      <!-- Migingo Island Boundary Hotspot -->
      <rect x="270" y="195" width="12" height="12" fill="{ACCENT_AMBER}" rx="2"/>
      <text x="276" y="225" fill="{ACCENT_AMBER}" font-size="9" font-weight="700" text-anchor="middle">Migingo Island (Dispute)</text>
    </g>

    <!-- Side Data Panel -->
    <g transform="translate(480, 70)">
      <rect width="320" height="330" fill="{PANEL_BG}" rx="10" stroke="{BORDER_COLOR}"/>
      <text x="20" y="30" fill="{ACCENT_GREEN}" font-size="14" font-weight="700">Lake Victoria Basin Facts</text>

      <text x="20" y="60" fill="{TEXT_MAIN}" font-size="11" font-weight="600">• Territorial Distribution:</text>
      <text x="30" y="80" fill="{TEXT_MUTED}" font-size="10">Tanzania: 49% | Uganda: 46% | Kenya: 6%</text>

      <text x="20" y="110" fill="{TEXT_MAIN}" font-size="11" font-weight="600">• Dominant Species Harvested:</text>
      <text x="30" y="130" fill="{ACCENT_BLUE}" font-size="10">1. Nile Perch (Export Fillets)</text>
      <text x="30" y="148" fill="{ACCENT_GREEN}" font-size="10">2. Tilapia (Domestic Table Fish)</text>
      <text x="30" y="166" fill="{ACCENT_AMBER}" font-size="10">3. Omena / Dagaa (Night Lantern)</text>

      <rect x="15" y="195" width="290" height="115" rx="8" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="25" y="220" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">Critical Lake Challenges:</text>
      <text x="25" y="240" fill="{TEXT_MAIN}" font-size="10">• Illegal small-meshed mosquito nets</text>
      <text x="25" y="258" fill="{TEXT_MAIN}" font-size="10">• Invasive Water Hyacinth mats</text>
      <text x="25" y="276" fill="{TEXT_MAIN}" font-size="10">• Exploitative middlemen &amp; cold chain lack</text>
      <text x="25" y="294" fill="{TEXT_MAIN}" font-size="10">• Cross-border security disputes (Migingo)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Spatial Layout, Landing Beaches, and Basin Catchment of Lake Victoria")

def svg_lake_victoria_hyacinth_predation():
    """SVG 13: Ecological Food Web Disruption & Invasive Hyacinth in Lake Victoria"""
    inner = f"""
    <!-- Left: Food Web Disruption (Nile Perch Predation) -->
    <g transform="translate(30, 65)">
      <rect width="360" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="180" y="28" fill="{ACCENT_RED}" font-size="13" font-weight="700" text-anchor="middle">1. Nile Perch Ecological Predation</text>
      
      <!-- Top Predator: Nile Perch -->
      <rect x="100" y="50" width="160" height="45" rx="6" fill="{PANEL_BG_2}" stroke="{ACCENT_RED}" stroke-width="2"/>
      <text x="180" y="77" fill="{TEXT_MAIN}" font-size="12" font-weight="700" text-anchor="middle">Nile Perch (Apex Predator)</text>

      <!-- Predation Arrows -->
      <line x1="140" y1="95" x2="100" y2="150" stroke="{ACCENT_RED}" stroke-width="3"/>
      <line x1="220" y1="95" x2="260" y2="150" stroke="{ACCENT_RED}" stroke-width="3"/>

      <!-- Prey Species -->
      <rect x="30" y="150" width="130" height="40" rx="6" fill="{PANEL_BG_2}" stroke="{ACCENT_AMBER}"/>
      <text x="95" y="175" fill="{TEXT_MAIN}" font-size="10" font-weight="600" text-anchor="middle">Native Tilapia</text>

      <rect x="200" y="150" width="130" height="40" rx="6" fill="{PANEL_BG_2}" stroke="{TEXT_MUTED}"/>
      <text x="265" y="175" fill="{TEXT_MUTED}" font-size="10" font-weight="600" text-anchor="middle">200+ Haplochromines</text>
      <text x="265" y="205" fill="{ACCENT_RED}" font-size="9" text-anchor="middle">(Mass Extinction)</text>

      <text x="180" y="270" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Ecological Imbalance</text>
      <text x="180" y="290" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Nile Perch decimation of native algal-eating fish</text>
      <text x="180" y="305" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">leads to massive lake deoxygenation</text>
    </g>

    <!-- Right: Water Hyacinth Impact -->
    <g transform="translate(420, 65)">
      <rect width="390" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="195" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">2. Invasive Water Hyacinth (*Eichhornia*)</text>

      <!-- Water Surface with Floating Green Hyacinth Blanket -->
      <rect x="30" y="60" width="330" height="50" fill="{ACCENT_GREEN}66" stroke="{ACCENT_GREEN}" stroke-width="2" rx="4"/>
      <text x="195" y="90" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">Floating Hyacinth Weed Mat</text>

      <!-- 4 Critical Disruptions -->
      <g transform="translate(30, 130)">
        <text x="10" y="20" fill="{ACCENT_RED}" font-size="11" font-weight="600">• Blocks Boat Navigation:</text>
        <text x="25" y="38" fill="{TEXT_MUTED}" font-size="10">Clogs bays and traps fishing vessels at landing sites.</text>

        <text x="10" y="65" fill="{ACCENT_RED}" font-size="11" font-weight="600">• Destroys Nets:</text>
        <text x="25" y="83" fill="{TEXT_MUTED}" font-size="10">Tangles and tears expensive nylon gill nets.</text>

        <text x="10" y="110" fill="{ACCENT_RED}" font-size="11" font-weight="600">• Blocks Sunlight &amp; Oxygen:</text>
        <text x="25" y="128" fill="{TEXT_MUTED}" font-size="10">Decomposing weeds deplete dissolved oxygen, killing fish.</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Ecological Food Web Disruption & Invasive Hyacinth in Lake Victoria")

def svg_aquaculture_pond_cross_section():
    """SVG 14: Engineering Cross-Section of an Aquaculture Fish Pond and Water Flow"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Stream Water Inlet (Left) -->
      <polygon points="20,40 100,40 100,70 20,70" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="60" y="60" fill="{ACCENT_BLUE}" font-size="10" font-weight="700" text-anchor="middle">Stream Intake</text>
      <line x1="100" y1="55" x2="160" y2="85" stroke="{ACCENT_BLUE}" stroke-width="4"/>

      <!-- Earthen Pond Basin with Clay Liner -->
      <polygon points="140,80 620,80 560,250 200,250" fill="{PANEL_BG_2}" stroke="{ACCENT_AMBER}" stroke-width="3"/>
      <!-- Water in Pond -->
      <polygon points="160,100 600,100 550,230 210,230" fill="{ACCENT_BLUE}33"/>
      <text x="380" y="130" fill="{ACCENT_BLUE}" font-size="14" font-weight="700" text-anchor="middle">Pond Water Volume (Tilapia / Catfish)</text>

      <!-- Impermeable Clay Layer Label -->
      <text x="380" y="275" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">Impermeable Clay / Clay-Loam Liner (Prevents Infiltration)</text>

      <!-- Monk Drainage Sluice (Right) -->
      <rect x="560" y="100" width="30" height="150" fill="{PANEL_BG}" stroke="{ACCENT_RED}" stroke-width="2"/>
      <text x="575" y="175" fill="{ACCENT_RED}" font-size="10" font-weight="700" transform="rotate(-90, 575, 175)">Monk Sluice</text>
      <!-- Drainage pipe out -->
      <rect x="590" y="230" width="80" height="20" fill="{ACCENT_TEAL}"/>
      <text x="630" y="245" fill="{PANEL_BG}" font-size="9" font-weight="700" text-anchor="middle">Drain Pipe</text>

      <!-- Oxygenating Aquatic Plants -->
      <path d="M 240,230 L 240,180 M 280,230 L 280,170" stroke="{ACCENT_GREEN}" stroke-width="3"/>
      <text x="260" y="160" fill="{ACCENT_GREEN}" font-size="9" text-anchor="middle">Oxygenating Plants</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Engineering Design and Hydraulic Features of an Earthen Aquaculture Fish Pond")

def svg_kenya_vs_japan_contrast():
    """SVG 15: Kenya vs Japan Fishing Technology and Oceanographic Setting Contrast"""
    inner = f"""
    <!-- Left: Kenya Fishery Model -->
    <g transform="translate(30, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="185" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">KENYA FISHING INDUSTRY</text>
      
      <rect x="20" y="50" width="330" height="90" fill="{PANEL_BG_2}" rx="6"/>
      <text x="185" y="80" fill="{ACCENT_BLUE}" font-size="12" font-weight="700" text-anchor="middle">Inland Freshwater Focus (Lake Victoria)</text>
      <text x="185" y="100" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">90% freshwater harvest vs 10% marine</text>
      <text x="185" y="120" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Narrow marine continental shelf; warm Mozambique current</text>

      <g transform="translate(20, 160)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• Fleet: Non-motorized wooden dhows &amp; canoes</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Gear: Manual gill nets, hook &amp; line, night lamps</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Market: Domestic table fish; limited cultural demand</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Processing: Sun-drying &amp; fresh export fillets</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Capital: Low capital; dependence on private middlemen</text>
      </g>
    </g>

    <!-- Right: Japan Fishery Model -->
    <g transform="translate(440, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="185" y="28" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">JAPAN FISHING INDUSTRY</text>
      
      <rect x="20" y="50" width="330" height="90" fill="{PANEL_BG_2}" rx="6"/>
      <text x="185" y="80" fill="{ACCENT_BLUE}" font-size="12" font-weight="700" text-anchor="middle">Deep-Sea Marine Superpower (NW Pacific)</text>
      <text x="185" y="100" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">1/6th of total global marine catch</text>
      <text x="185" y="120" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Broad continental shelf; Kuroshiwo + Oyashiwo upwelling</text>

      <g transform="translate(20, 160)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• Fleet: Giant computerized factory trawlers</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Gear: Automated purse seines, sonar, radar tracking</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Market: Massive universal daily staple diet</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Processing: Automated filleting &amp; blast-freezing at sea</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Capital: Massive bank financing &amp; powerful co-operatives</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Comparative Analysis: Kenya vs Japan Fishing Industries")

def svg_seven_conservation_strategies():
    """SVG 16: The Seven Core Strategies for Sustainable Fisheries Conservation"""
    inner = f"""
    <!-- Central Strategy Box -->
    <g transform="translate(280, 190)">
      <rect width="280" height="60" rx="10" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2.5"/>
      <text x="140" y="28" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">SUSTAINABLE FISHERIES</text>
      <text x="140" y="48" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">CONSERVATION PILLARS</text>
    </g>

    <!-- 7 Surrounding Strategy Nodes -->
    <!-- 1. Banning Mosquito Nets -->
    <g transform="translate(40, 70)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_RED}"/>
      <text x="105" y="25" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">1. Net Mesh Regulation</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Banning small-meshed mosquito nets</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">to protect juvenile breeding stock</text>
    </g>

    <!-- 2. Closed Breeding Seasons -->
    <g transform="translate(315, 60)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="105" y="25" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">2. Closed Seasons</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Temporary fishing bans during</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">active spawning periods</text>
    </g>

    <!-- 3. Licensing & Catch Quotas -->
    <g transform="translate(590, 70)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}"/>
      <text x="105" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">3. Licensing &amp; Quotas</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Controlling extraction with Total</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Allowable Catch limits</text>
    </g>

    <!-- 4. Artificial Restocking -->
    <g transform="translate(40, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_TEAL}"/>
      <text x="105" y="25" fill="{ACCENT_TEAL}" font-size="11" font-weight="700" text-anchor="middle">4. Lake Restocking</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Releasing hatchery fingerlings</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">into overfished natural lakes</text>
    </g>

    <!-- 5. Promoting Aquaculture -->
    <g transform="translate(315, 310)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}"/>
      <text x="105" y="25" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">5. Aquaculture Ponds</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Promoting fish farming to relieve</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">pressure on wild fisheries</text>
    </g>

    <!-- 6. Infrastructure & Roads -->
    <g transform="translate(590, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}"/>
      <text x="105" y="25" fill="{ACCENT_PURPLE}" font-size="11" font-weight="700" text-anchor="middle">6. Road Infrastructure</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Tarmacking Kitale–Kalokol road</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">to open underutilized lakes</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="The Seven Core Strategies for Sustainable Fisheries Conservation in Kenya")


# =============================================================================
# ENRICHMENT PIPELINE
# =============================================================================

def run_enrichment():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 2: Visual Enrichment Engine")
    print("Attaching 16 Vector SVGs & 6 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    topic = Topic.objects.filter(name="Fishing").first()
    if not topic:
        print("[!] Error: Topic 2 'Fishing' not found. Run ingest_form4_geography_topic2.py first.")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    if len(lessons) < 6:
        print(f"[!] Warning: Found {len(lessons)} lessons (expected 6).")

    lesson_1 = lessons[0]  # Foundations
    lesson_2 = lessons[1]  # Classification & Traditional Methods
    lesson_3 = lessons[2]  # Commercial Methods & Ecology
    lesson_4 = lessons[3]  # Major World Fishing Grounds
    lesson_5 = lessons[4]  # East African & Kenyan Fisheries
    lesson_6 = lessons[5]  # Comparative Analysis & Management

    # Clear existing LessonAssets for clean enrichment
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean enrichment.")

    # -------------------------------------------------------------------------
    # LESSON 1 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 1: {lesson_1.title}")
    attach_svg_to_block(lesson_1, "Continental Shelf & Photic Zone Cross-Section", svg_photic_zone_continental_shelf)
    attach_svg_to_block(lesson_1, "Ocean Current Convergence & Nutrient Upwelling Mechanism", svg_current_convergence_upwelling)
    attach_wikimedia_to_block(
        lesson=lesson_1,
        exact_title="Glaciated Fiord Coastline in Norway Providing Natural Sheltered Inlets",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/6/6c/Geirangerfjord_LC0188.jpg",
        author="Jörg Hempel / Wikimedia Commons",
        licensing="CC BY-SA 2.0 de",
        commons_page="https://commons.wikimedia.org/wiki/File:Geirangerfjord_LC0188.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 2 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 2: {lesson_2.title}")
    attach_svg_to_block(lesson_2, "The Four Types of Fishing Taxonomy Tree & Depth Profile", svg_four_fishery_types)
    attach_svg_to_block(lesson_2, "Mechanics of Traditional Basket Trap and Gill Netting", svg_basket_and_gillnet)
    attach_wikimedia_to_block(
        lesson=lesson_2,
        exact_title="Traditional Wooden Dhows on the Coastal Waters of Kenya",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/e/e3/Traditional_Dhows_%28Dau%29_of_Coastal_Kenya.jpg",
        author="MariamSaria",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Traditional_Dhows_(Dau)_of_Coastal_Kenya.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 3 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 3: {lesson_3.title}")
    attach_svg_to_block(lesson_3, "Operational Mechanics of Purse Seining (Surface Pelagic)", svg_purse_seining)
    attach_svg_to_block(lesson_3, "Bottom Trawling Operations and Benthic Habitat Disruption", svg_bottom_trawling)
    attach_wikimedia_to_block(
        lesson=lesson_3,
        exact_title="Commercial Trawler Winching Up a Heavy Marine Net",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Fishing_net_of_a_trawler_%281%29.jpg",
        author="Ibex73",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Fishing_net_of_a_trawler_(1).jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 4 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 4: {lesson_4.title}")
    attach_svg_to_block(lesson_4, "Global Thematic Map of Major World Fishing Grounds & Ocean Currents", svg_world_fishing_grounds)
    attach_svg_to_block(lesson_4, "Spatial Map of the Northwest Atlantic & Grand Bank Current Convergence", svg_nw_atlantic_grand_bank)
    attach_svg_to_block(lesson_4, "Spatial Map of the Northwest Pacific Ground & Kuroshiwo/Oyashiwo Convergence", svg_nw_pacific_japan)
    attach_wikimedia_to_block(
        lesson=lesson_4,
        exact_title="Coho Salmon Spawning Run in the Pacific Northwest Rushing Rivers",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/5/53/Coho_Spawning_on_the_Salmon_River_%2816150184519%29.jpg",
        author="Bureau of Land Management Oregon and Washington",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:Coho_Spawning_on_the_Salmon_River_(16150184519).jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 5 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 5: {lesson_5.title}")
    attach_svg_to_block(lesson_5, "Profile of the Kenyan Marine Coastline (Narrow Shelf vs Indian Ocean)", svg_kenya_marine_profile)
    attach_svg_to_block(lesson_5, "Spatial Map of Inland Freshwater Fisheries and Hatcheries in Kenya", svg_kenya_inland_fisheries_map)
    attach_svg_to_block(lesson_5, "Lake Victoria Basin, Catchment, and Major Landing Beaches", svg_lake_victoria_basin)
    attach_svg_to_block(lesson_5, "Ecological Food Web Disruption & Invasive Hyacinth in Lake Victoria", svg_lake_victoria_hyacinth_predation)
    attach_svg_to_block(lesson_5, "Engineering Cross-Section of an Aquaculture Fish Pond and Water Flow", svg_aquaculture_pond_cross_section)
    attach_wikimedia_to_block(
        lesson=lesson_5,
        exact_title="Artisanal Wooden Fishing Boats and Operations on Lake Victoria in Kisumu",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Fishing_activities_at_Lake_Victoria_in_Kisumu.jpg",
        author="VickyOmondi",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Fishing_activities_at_Lake_Victoria_in_Kisumu.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 6 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 6: {lesson_6.title}")
    attach_svg_to_block(lesson_6, "Kenya vs Japan Fishing Technology and Oceanographic Setting Contrast", svg_kenya_vs_japan_contrast)
    attach_svg_to_block(lesson_6, "The Seven Core Strategies for Sustainable Fisheries Conservation", svg_seven_conservation_strategies)
    attach_wikimedia_to_block(
        lesson=lesson_6,
        exact_title="Commercial Tuna Auction and Processing at Tsukiji Fish Market in Japan",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/August_2007_Tsukiji_fish_market_27.jpg",
        author="Syced",
        licensing="CC0 (Public domain)",
        commons_page="https://commons.wikimedia.org/wiki/File:August_2007_Tsukiji_fish_market_27.jpg"
    )

    print("\n" + "=" * 80)
    print("[SUCCESS] Form 4 Geography Topic 2 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {LessonAsset.objects.filter(lesson__in=lessons).count()}")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment()
