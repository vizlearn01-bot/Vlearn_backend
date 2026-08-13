"""
VLearn Form 4 Geography — Topic 3: Wildlife and Tourism
Visual Enrichment Engine (16 High-Precision Vector SVGs & 6 Verified Wikimedia Photographic Assets)

Topic: Wildlife and Tourism (Topic ID: 58)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)

Visual Inventory:
  Lesson 1:
    - SVG 1: Ecological Factor Web of East African Wildlife Distribution
    - SVG 2: Relief and Aspect Profile: Windward Forest vs Leeward Rain-Shadow Savanna
    - Wikimedia 1: Thomson's Gazelle in the Open Savanna Plains of Amboseli National Park
  Lesson 2:
    - SVG 3: Classification Hierarchy of Protected Areas (Parks, Reserves, Sanctuaries)
    - SVG 4: Zonation and Land-Use Boundaries of a National Park vs Game Reserve
    - SVG 5: Specialized Sanctuary Architecture & Captive Breeding Cycle
    - Wikimedia 2: Endangered Black Rhinoceros in Lake Nakuru Protected Sanctuary
  Lesson 3:
    - SVG 6: Threat Matrix: Human-Induced vs Natural Pressures on East African Wildlife
    - SVG 7: The KWS Wildlife Management vs Conservation Strategic Framework
    - SVG 8: Step-by-Step Logistics of KWS Animal Translocation Process
    - Wikimedia 3: Kenya Wildlife Service (KWS) Ranger Briefing and Conservation Patrols
  Lesson 4:
    - SVG 9: The Five Pillars of Eco-Tourism Operation
    - SVG 10: Push-Pull Dynamics of International Tourism to Tropical Kenya
    - Wikimedia 4: Historical Fort Jesus Built in 1593 in Coastal Mombasa
  Lesson 5:
    - SVG 11: Thematic Map of Kenya: Spatial Distribution of Coastal vs Inland Tourist Hubs
    - SVG 12: Transect of the Kenyan Coastal Strip: Coral Reefs, Beaches, Mangroves, and Kayas
    - SVG 13: Economic Multiplier Effect of Tourism in Kenya
    - Wikimedia 5: The Great Wildebeest Migration in Maasai Mara Game Reserve
  Lesson 6:
    - SVG 14: Physical and Technological Infrastructure of Swiss Alpine Tourism
    - SVG 15: Comparative Matrix: Kenya Tropical Savanna vs Switzerland Alpine Ecosystems
    - SVG 16: Six-Point Strategic Action Plan for Kenyan Tourism Sector Expansion
    - Wikimedia 6: Modern Electrified Cable Car Transit Ascending the Swiss Alps with Matterhorn View

Usage:
  ./venv/bin/python curriculum/enrich_form4_geography_topic3.py
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
# 16 HIGH-PRECISION SVG BUILDERS FOR TOPIC 3
# =============================================================================

def svg_ecological_factor_web():
    """SVG 1: Ecological Factor Web of East African Wildlife Distribution"""
    inner = f"""
    <!-- Central Node: Wildlife Distribution -->
    <g transform="translate(300, 180)">
      <rect width="240" height="60" rx="10" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2.5"/>
      <text x="120" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">WILDLIFE DISTRIBUTION</text>
      <text x="120" y="48" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">East African Zonation</text>
    </g>

    <!-- 5 Factor Nodes Surrounding -->
    <!-- 1. Climate (Top Left) -->
    <g transform="translate(40, 60)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}"/>
      <text x="105" y="25" fill="{ACCENT_BLUE}" font-size="12" font-weight="700" text-anchor="middle">1. Climate &amp; Rainfall</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">High rain -> Montane Forest</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Low rain -> Thorny Savanna</text>
      <line x1="210" y1="50" x2="300" y2="180" stroke="{ACCENT_BLUE}" stroke-width="1.5" stroke-dasharray="3,3"/>
    </g>

    <!-- 2. Relief & Aspect (Top Right) -->
    <g transform="translate(590, 60)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="105" y="25" fill="{ACCENT_AMBER}" font-size="12" font-weight="700" text-anchor="middle">2. Relief &amp; Aspect</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Windward -> Forest Browsers</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Leeward -> Cheetah Plains</text>
      <line x1="0" y1="50" x2="-50" y2="120" stroke="{ACCENT_AMBER}" stroke-width="1.5" stroke-dasharray="3,3"/>
    </g>

    <!-- 3. Soils (Bottom Left) -->
    <g transform="translate(40, 290)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}"/>
      <text x="105" y="25" fill="{ACCENT_PURPLE}" font-size="12" font-weight="700" text-anchor="middle">3. Soil Quality &amp; Depth</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Volcanic -> Multi-tier Forest</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Shallow -> Savanna Grazing</text>
      <line x1="210" y1="20" x2="300" y2="-50" stroke="{ACCENT_PURPLE}" stroke-width="1.5" stroke-dasharray="3,3"/>
    </g>

    <!-- 4. Vegetation Biomes (Bottom Center) -->
    <g transform="translate(315, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_TEAL}"/>
      <text x="105" y="25" fill="{ACCENT_TEAL}" font-size="12" font-weight="700" text-anchor="middle">4. Vegetation Cover</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Acacia -> Giraffe Browse</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Canopy -> Arboreal Primates</text>
      <line x1="105" y1="0" x2="105" y2="-60" stroke="{ACCENT_TEAL}" stroke-width="1.5"/>
    </g>

    <!-- 5. Water Sources (Bottom Right) -->
    <g transform="translate(590, 290)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_RED}"/>
      <text x="105" y="25" fill="{ACCENT_RED}" font-size="12" font-weight="700" text-anchor="middle">5. Water &amp; Human Land-Use</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Permanent Lakes -> Hippos</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Parks vs Human Settlements</text>
      <line x1="0" y1="20" x2="-50" y2="-50" stroke="{ACCENT_RED}" stroke-width="1.5" stroke-dasharray="3,3"/>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Ecological Factor Web Controlling Wildlife Distribution in East Africa")

def svg_windward_leeward_profile():
    """SVG 2: Relief and Aspect Profile: Windward Forest vs Leeward Rain-Shadow Savanna"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Mountain Profile -->
      <path d="M 20,320 L 260,110 L 400,60 L 540,180 L 740,320 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}" stroke-width="2"/>
      
      <!-- Mountain Peak -->
      <polygon points="380,80 400,60 420,80" fill="{TEXT_MAIN}"/>
      <text x="400" y="45" fill="{TEXT_MAIN}" font-size="12" font-weight="700" text-anchor="middle">Volcanic Mountain Peak (e.g. Mt. Kenya)</text>

      <!-- Windward Side (Left) -->
      <!-- Moist Winds & Rain Clouds -->
      <g stroke="{ACCENT_BLUE}" stroke-width="3">
        <line x1="40" y1="260" x2="100" y2="230"/>
        <line x1="60" y1="290" x2="120" y2="260"/>
        <line x1="80" y1="230" x2="140" y2="200"/>
      </g>
      <text x="100" y="160" fill="{ACCENT_BLUE}" font-size="12" font-weight="700">Moist Prevailing Winds</text>
      <text x="100" y="180" fill="{ACCENT_BLUE}" font-size="10">(Orographic Rainfall)</text>

      <!-- Montane Forest & Browsers (Left Slope) -->
      <rect x="140" y="190" width="130" height="70" rx="6" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}"/>
      <text x="205" y="215" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">Windward Slope</text>
      <text x="205" y="235" fill="{TEXT_MAIN}" font-size="10" text-anchor="middle">Dense Montane Forest</text>
      <text x="205" y="250" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Elephants, Buffaloes, Primates</text>

      <!-- Leeward Side (Right) -->
      <!-- Descending Dry Air -->
      <path d="M 450,90 Q 520,130 580,210" fill="none" stroke="{ACCENT_AMBER}" stroke-width="3" stroke-dasharray="4,4"/>
      <text x="560" y="130" fill="{ACCENT_AMBER}" font-size="12" font-weight="700">Dry Descending Air</text>
      <text x="560" y="150" fill="{ACCENT_AMBER}" font-size="10">(Rain Shadow Zone)</text>

      <!-- Savanna Plains & Cursorial Hunters (Right Slope) -->
      <rect x="520" y="220" width="190" height="85" rx="6" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="615" y="245" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">Leeward Rain-Shadow Savanna</text>
      <text x="615" y="265" fill="{TEXT_MAIN}" font-size="10" text-anchor="middle">Open Grassland &amp; Acacia Scrub</text>
      <text x="615" y="280" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Fast Plains: Cheetahs, Lions, Zebras</text>
      <text x="615" y="295" fill="{ACCENT_GREEN}" font-size="9" text-anchor="middle">(e.g. Amboseli Plains)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Mountain Aspect and Relief Profile: Windward Forest vs Leeward Savanna Plains")

def svg_protected_areas_taxonomy():
    """SVG 3: Classification Hierarchy of Protected Areas (Parks, Reserves, Sanctuaries)"""
    inner = f"""
    <!-- Root Header -->
    <g transform="translate(260, 60)">
      <rect width="320" height="45" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="160" y="28" fill="{TEXT_MAIN}" font-size="14" font-weight="700" text-anchor="middle">EAST AFRICAN PROTECTED AREAS</text>
    </g>

    <!-- Branch Connector Lines -->
    <line x1="420" y1="105" x2="420" y2="125" stroke="{BORDER_COLOR}" stroke-width="2"/>
    <line x1="140" y1="125" x2="700" y2="125" stroke="{BORDER_COLOR}" stroke-width="2"/>
    <line x1="140" y1="125" x2="140" y2="145" stroke="{ACCENT_GREEN}" stroke-width="2"/>
    <line x1="420" y1="125" x2="420" y2="145" stroke="{ACCENT_AMBER}" stroke-width="2"/>
    <line x1="700" y1="125" x2="700" y2="145" stroke="{ACCENT_PURPLE}" stroke-width="2"/>

    <!-- 3 Category Cards -->
    <!-- 1. National Park -->
    <g transform="translate(40, 145)">
      <rect width="220" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="110" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">1. NATIONAL PARK</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10.5">• Statute: Act of Parliament</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10.5">• Management: National Gov (KWS)</text>
      <text x="15" y="95" fill="{ACCENT_RED}" font-size="10.5">• Land-Use: Strict Single-Use</text>
      <text x="15" y="115" fill="{TEXT_MUTED}" font-size="10">• Grazing/Settlement: BANNED</text>
      <text x="15" y="135" fill="{TEXT_MUTED}" font-size="10">• Fencing: Fully enclosed</text>
      <text x="15" y="165" fill="{ACCENT_GREEN}" font-size="11" font-weight="700">Examples:</text>
      <text x="15" y="185" fill="{TEXT_MAIN}" font-size="10">Tsavo, Amboseli, Nairobi,</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">Mt. Kenya, Lake Nakuru</text>
    </g>

    <!-- 2. Game Reserve -->
    <g transform="translate(310, 145)">
      <rect width="220" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <text x="110" y="28" fill="{ACCENT_AMBER}" font-size="13" font-weight="700" text-anchor="middle">2. GAME RESERVE</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10.5">• Statute: County Council By-Law</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10.5">• Management: Local County Gov</text>
      <text x="15" y="95" fill="{ACCENT_GREEN}" font-size="10.5">• Land-Use: Multi-Use Zone</text>
      <text x="15" y="115" fill="{TEXT_MUTED}" font-size="10">• Grazing: Allowed (Seasonal)</text>
      <text x="15" y="135" fill="{TEXT_MUTED}" font-size="10">• Fencing: Unfenced migration</text>
      <text x="15" y="165" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">Examples:</text>
      <text x="15" y="185" fill="{TEXT_MAIN}" font-size="10">Maasai Mara, Samburu,</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">Selous (Tanzania)</text>
    </g>

    <!-- 3. Game Sanctuary -->
    <g transform="translate(580, 145)">
      <rect width="220" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}" stroke-width="2"/>
      <text x="110" y="28" fill="{ACCENT_PURPLE}" font-size="13" font-weight="700" text-anchor="middle">3. GAME SANCTUARY</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10.5">• Statute: Endangered Species Law</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10.5">• Focus: Specific Rare Species</text>
      <text x="15" y="95" fill="{ACCENT_PURPLE}" font-size="10.5">• Security: Predator Elimination</text>
      <text x="15" y="115" fill="{TEXT_MUTED}" font-size="10">• Purpose: Captive Breeding</text>
      <text x="15" y="135" fill="{TEXT_MUTED}" font-size="10">• Release: Translocation to parks</text>
      <text x="15" y="165" fill="{ACCENT_PURPLE}" font-size="11" font-weight="700">Examples:</text>
      <text x="15" y="185" fill="{TEXT_MAIN}" font-size="10">Kisumu Impala Sanctuary,</text>
      <text x="15" y="200" fill="{TEXT_MAIN}" font-size="10">L. Nakuru Rhino Sanctuary</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Administrative, Legal, and Land-Use Classification of Protected Areas")

def svg_park_vs_reserve_zonation():
    """SVG 4: Zonation and Land-Use Boundaries of a National Park vs Game Reserve"""
    inner = f"""
    <!-- Left: National Park (Strict Fenced Single-Use) -->
    <g transform="translate(30, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="185" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">NATIONAL PARK: SINGLE-USE ZONATION</text>

      <!-- Fenced Wildlife Core -->
      <rect x="25" y="55" width="320" height="210" rx="6" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="185" y="85" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">Pristine Wildlife Core Habitat</text>
      <text x="185" y="105" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Elephants, Lions, Rhinos, Zebras</text>

      <!-- Electric Perimeter Fence Graphic -->
      <rect x="20" y="50" width="330" height="220" fill="none" stroke="{ACCENT_AMBER}" stroke-width="3" stroke-dasharray="6,4"/>
      <text x="185" y="140" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">⚡ Solar Electric Perimeter Fence ⚡</text>

      <!-- Prohibited Signs -->
      <g transform="translate(45, 170)">
        <rect width="280" height="60" fill="{PANEL_BG}" rx="4" stroke="{ACCENT_RED}"/>
        <text x="140" y="25" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">STRICTLY PROHIBITED:</text>
        <text x="140" y="45" fill="{TEXT_MAIN}" font-size="10" text-anchor="middle">No Cattle Grazing | No Settlement | No Farming</text>
      </g>

      <text x="185" y="300" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Managed Directly by National Government (KWS)</text>
    </g>

    <!-- Right: Game Reserve (Multi-Use Coexistence) -->
    <g transform="translate(440, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
      <text x="185" y="28" fill="{ACCENT_AMBER}" font-size="13" font-weight="700" text-anchor="middle">GAME RESERVE: MULTI-USE ZONATION</text>

      <!-- Multi-Use Core -->
      <rect x="25" y="55" width="320" height="130" rx="6" fill="{PANEL_BG_2}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <text x="185" y="85" fill="{ACCENT_AMBER}" font-size="12" font-weight="700" text-anchor="middle">Wildlife Conservation Core</text>
      <text x="185" y="105" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Wildebeest, Zebras, Predators</text>

      <!-- Shared Grazing Buffer Zone -->
      <g transform="translate(25, 195)">
        <rect width="320" height="85" rx="6" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}"/>
        <text x="160" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">Regulated Seasonal Grazing Buffer</text>
        <text x="160" y="45" fill="{TEXT_MAIN}" font-size="10" text-anchor="middle">Local Maasai Pastoralist Herds (Dry Season)</text>
        <text x="160" y="65" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Shared Waterholes &amp; Open Migration Corridors</text>
      </g>

      <text x="185" y="315" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Managed by Local County Government (e.g. Narok)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Comparative Spatial Zonation: Fenced National Park vs Multi-Use Game Reserve")

def svg_sanctuary_architecture_breeding():
    """SVG 5: Specialized Sanctuary Architecture & Captive Breeding Cycle"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Outer Fortified Perimeter -->
      <rect x="20" y="30" width="720" height="300" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}" stroke-width="2.5"/>
      <text x="380" y="20" fill="{ACCENT_PURPLE}" font-size="13" font-weight="700" text-anchor="middle">High-Security Specialized Game Sanctuary (e.g. Lake Nakuru Rhino Sanctuary)</text>

      <!-- Zone 1: Veterinary Hospital & Orphan Nursery (Left) -->
      <g transform="translate(40, 50)">
        <rect width="180" height="260" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_RED}"/>
        <text x="90" y="25" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">1. Vet Clinic &amp; Nursery</text>
        <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10">• Abandoned calf care</text>
        <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10">• Bottle-feeding station</text>
        <text x="15" y="95" fill="{TEXT_MAIN}" font-size="10">• Microchip horn tagging</text>
        <text x="15" y="125" fill="{ACCENT_RED}" font-size="10" font-weight="600">Predator Exclusion:</text>
        <text x="15" y="145" fill="{TEXT_MUTED}" font-size="9">Lions &amp; hyenas strictly</text>
        <text x="15" y="160" fill="{TEXT_MUTED}" font-size="9">removed to save calves</text>
      </g>

      <!-- Zone 2: Intensive Breeding Paddocks (Center) -->
      <g transform="translate(240, 50)">
        <rect width="280" height="260" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}"/>
        <text x="140" y="25" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">2. Protected Breeding Paddocks</text>
        <circle cx="140" cy="110" r="50" fill="{ACCENT_GREEN}22" stroke="{ACCENT_GREEN}" stroke-width="2"/>
        <text x="140" y="105" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">Endangered Black Rhinos</text>
        <text x="140" y="125" fill="{ACCENT_GREEN}" font-size="10" text-anchor="middle">Population Doubling Zone</text>
        <text x="20" y="190" fill="{TEXT_MAIN}" font-size="10">• 24/7 Armed Ranger Patrols</text>
        <text x="20" y="210" fill="{TEXT_MAIN}" font-size="10">• Solar Borehole Water Troughs</text>
        <text x="20" y="230" fill="{TEXT_MAIN}" font-size="10">• Anti-Poaching Drone Surveillance</text>
      </g>

      <!-- Zone 3: Release & Translocation Corridor (Right) -->
      <g transform="translate(540, 50)">
        <rect width="180" height="260" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}"/>
        <text x="90" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">3. Release Corridor</text>
        <line x1="20" y1="130" x2="160" y2="130" stroke="{ACCENT_BLUE}" stroke-width="3"/>
        <polygon points="150,125 165,130 150,135" fill="{ACCENT_BLUE}"/>
        <text x="90" y="105" fill="{ACCENT_BLUE}" font-size="10" font-weight="700" text-anchor="middle">Translocation Outflow</text>
        <text x="15" y="170" fill="{TEXT_MAIN}" font-size="10">• Mature stock crated</text>
        <text x="15" y="190" fill="{TEXT_MAIN}" font-size="10">• Released into wild</text>
        <text x="15" y="205" fill="{TEXT_MAIN}" font-size="10">  National Parks (Tsavo)</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Architectural Layout and Captive Breeding Recovery Cycle in a Game Sanctuary")

def svg_threat_matrix_dual_column():
    """SVG 6: Threat Matrix: Human-Induced vs Natural Pressures on East African Wildlife"""
    inner = f"""
    <!-- Left Column: Human-Induced Threats -->
    <g transform="translate(30, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_RED}" stroke-width="2"/>
      <text x="185" y="28" fill="{ACCENT_RED}" font-size="13" font-weight="700" text-anchor="middle">HUMAN-INDUCED THREATS</text>

      <g transform="translate(20, 55)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_RED}" font-size="11" font-weight="700">1. Commercial Trophy Poaching</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Illegal ivory tusks &amp; rhino horns for black market</text>
      </g>

      <g transform="translate(20, 120)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_RED}" font-size="11" font-weight="700">2. Habitat Fragmentation &amp; Encroachment</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Farming &amp; urban expansion blocking migration corridors</text>
      </g>

      <g transform="translate(20, 185)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_RED}" font-size="11" font-weight="700">3. Industrial &amp; Sewage Water Pollution</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Toxic runoff poisoning Rift lakes (Lake Nakuru flamingos)</text>
      </g>

      <g transform="translate(20, 250)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_RED}" font-size="11" font-weight="700">4. Off-Road Safari Vehicle Stress</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Acoustic noise &amp; soil compaction disrupting predators</text>
      </g>
    </g>

    <!-- Right Column: Natural Threats -->
    <g transform="translate(440, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <text x="185" y="28" fill="{ACCENT_AMBER}" font-size="13" font-weight="700" text-anchor="middle">NATURAL ENVIRONMENTAL THREATS</text>

      <g transform="translate(20, 55)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">1. Severe Prolonged Drought</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Depletion of browse &amp; waterholes causing mass starvation</text>
      </g>

      <g transform="translate(20, 120)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">2. Uncontrolled Bushfires</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Lightning fires incinerating vegetation &amp; slow wildlife</text>
      </g>

      <g transform="translate(20, 185)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">3. Epizootic Wildlife Diseases</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">FIV in lions, Anthrax, and Rinderpest outbreaks</text>
      </g>

      <g transform="translate(20, 250)">
        <rect width="330" height="55" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
        <text x="15" y="22" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">4. Flash Flooding &amp; Soil Erosion</text>
        <text x="15" y="40" fill="{TEXT_MUTED}" font-size="9.5">Submergence of low-lying floodplains drowning animals</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Threat Matrix: Human-Induced Pressures vs Natural Environmental Shocks")

def svg_management_vs_conservation_framework():
    """SVG 7: The KWS Wildlife Management vs Conservation Strategic Framework"""
    inner = f"""
    <!-- Root Header -->
    <g transform="translate(260, 60)">
      <rect width="320" height="45" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="160" y="28" fill="{TEXT_MAIN}" font-size="13" font-weight="700" text-anchor="middle">KWS WILDLIFE PROTECTION FRAMEWORK</text>
    </g>

    <!-- Bifurcation Lines -->
    <line x1="420" y1="105" x2="420" y2="125" stroke="{BORDER_COLOR}" stroke-width="2"/>
    <line x1="210" y1="125" x2="630" y2="125" stroke="{BORDER_COLOR}" stroke-width="2"/>
    <line x1="210" y1="125" x2="210" y2="145" stroke="{ACCENT_GREEN}" stroke-width="2"/>
    <line x1="630" y1="125" x2="630" y2="145" stroke="{ACCENT_RED}" stroke-width="2"/>

    <!-- Left: Management Policies (Active Manipulation) -->
    <g transform="translate(30, 145)">
      <rect width="360" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="180" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">WILDLIFE MANAGEMENT (Active Planning)</text>
      
      <g transform="translate(15, 45)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• Public Conservation Education &amp; Media</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• School Wildlife Clubs of Kenya (WCK)</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Game Ranching &amp; Farming (Ostrich / Crocodiles)</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Controlled Scientific Culling of Overaged Herds</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Animal Translocation from Overcrowded Parks</text>
        <text x="0" y="145" fill="{TEXT_MAIN}" font-size="10.5">• Promoting Discounted Domestic Tourism</text>
      </g>
    </g>

    <!-- Right: Conservation Policies (Strict Legal Protection) -->
    <g transform="translate(450, 145)">
      <rect width="360" height="240" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_RED}" stroke-width="2"/>
      <text x="180" y="28" fill="{ACCENT_RED}" font-size="13" font-weight="700" text-anchor="middle">WILDLIFE CONSERVATION (Preservation)</text>

      <g transform="translate(15, 45)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• Absolute Ban on Sport &amp; Trophy Hunting (1977)</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Total Prohibition of Ivory &amp; Skin Trade (CITES)</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Gazettement of National Parks &amp; Forest Reserves</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Setting up Fortified Rhino Sanctuaries</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Paramilitary Armed Anti-Poaching Ranger Units</text>
        <text x="0" y="145" fill="{TEXT_MAIN}" font-size="10.5">• Solar-Powered Electric Perimeter Fencing</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Bifurcated Strategic Framework: Wildlife Management vs Wildlife Conservation")

def svg_translocation_logistics():
    """SVG 8: Step-by-Step Logistics of KWS Animal Translocation Process"""
    inner = f"""
    <!-- 5 Sequential Logistics Steps -->
    <g transform="translate(20, 65)">
      <!-- Step 1 -->
      <g transform="translate(0, 0)">
        <rect width="145" height="330" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="72" y="25" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">Step 1: Audit</text>
        <rect x="15" y="45" width="115" height="60" rx="4" fill="{PANEL_BG_2}"/>
        <text x="72" y="75" fill="{ACCENT_RED}" font-size="9" font-weight="700" text-anchor="middle">Overpopulation</text>
        <text x="72" y="90" fill="{TEXT_MUTED}" font-size="8" text-anchor="middle">Habitat stress detected</text>
        <text x="10" y="135" fill="{TEXT_MUTED}" font-size="9.5">• Tree debarking</text>
        <text x="10" y="155" fill="{TEXT_MUTED}" font-size="9.5">• Severe soil erosion</text>
        <text x="10" y="175" fill="{TEXT_MUTED}" font-size="9.5">• Herd stress survey</text>
      </g>

      <!-- Step 2 -->
      <g transform="translate(160, 0)">
        <rect width="145" height="330" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="72" y="25" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">Step 2: Mapping</text>
        <rect x="15" y="45" width="115" height="60" rx="4" fill="{PANEL_BG_2}"/>
        <text x="72" y="75" fill="{ACCENT_AMBER}" font-size="9" font-weight="700" text-anchor="middle">Recipient Park</text>
        <text x="72" y="90" fill="{TEXT_MUTED}" font-size="8" text-anchor="middle">Underpopulated zones</text>
        <text x="10" y="135" fill="{TEXT_MUTED}" font-size="9.5">• Browse capacity</text>
        <text x="10" y="155" fill="{TEXT_MUTED}" font-size="9.5">• Water hole survey</text>
        <text x="10" y="175" fill="{TEXT_MUTED}" font-size="9.5">• Security readiness</text>
      </g>

      <!-- Step 3 -->
      <g transform="translate(320, 0)">
        <rect width="145" height="330" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="72" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">Step 3: Sedation</text>
        <rect x="15" y="45" width="115" height="60" rx="4" fill="{PANEL_BG_2}"/>
        <text x="72" y="75" fill="{ACCENT_BLUE}" font-size="9" font-weight="700" text-anchor="middle">Helicopter Dart</text>
        <text x="72" y="90" fill="{TEXT_MUTED}" font-size="8" text-anchor="middle">Vet tranquilizer</text>
        <text x="10" y="135" fill="{TEXT_MUTED}" font-size="9.5">• Air tracking</text>
        <text x="10" y="155" fill="{TEXT_MUTED}" font-size="9.5">• Fast sedation</text>
        <text x="10" y="175" fill="{TEXT_MUTED}" font-size="9.5">• Vital signs check</text>
      </g>

      <!-- Step 4 -->
      <g transform="translate(480, 0)">
        <rect width="145" height="330" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="72" y="25" fill="{ACCENT_PURPLE}" font-size="11" font-weight="700" text-anchor="middle">Step 4: Transit</text>
        <rect x="15" y="45" width="115" height="60" rx="4" fill="{PANEL_BG_2}"/>
        <text x="72" y="75" fill="{ACCENT_PURPLE}" font-size="9" font-weight="700" text-anchor="middle">Heavy Crating</text>
        <text x="72" y="90" fill="{TEXT_MUTED}" font-size="8" text-anchor="middle">Hydraulic truck lift</text>
        <text x="10" y="135" fill="{TEXT_MUTED}" font-size="9.5">• Specialized trucks</text>
        <text x="10" y="155" fill="{TEXT_MUTED}" font-size="9.5">• Vet team on board</text>
        <text x="10" y="175" fill="{TEXT_MUTED}" font-size="9.5">• Highway escort</text>
      </g>

      <!-- Step 5 -->
      <g transform="translate(640, 0)">
        <rect width="145" height="330" rx="8" fill="{PANEL_BG}" stroke="{BORDER_COLOR}"/>
        <text x="72" y="25" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">Step 5: Release</text>
        <rect x="15" y="45" width="115" height="60" rx="4" fill="{PANEL_BG_2}"/>
        <text x="72" y="75" fill="{ACCENT_GREEN}" font-size="9" font-weight="700" text-anchor="middle">GPS Tracking</text>
        <text x="72" y="90" fill="{TEXT_MUTED}" font-size="8" text-anchor="middle">Satellite collars</text>
        <text x="10" y="135" fill="{TEXT_MUTED}" font-size="9.5">• Revive medication</text>
        <text x="10" y="155" fill="{TEXT_MUTED}" font-size="9.5">• Solar GPS collar</text>
        <text x="10" y="175" fill="{TEXT_MUTED}" font-size="9.5">• Herd integration</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Five-Stage Operational Protocol for KWS Large Herbivore Translocation")

def svg_ecotourism_five_pillars():
    """SVG 9: The Five Pillars of Eco-Tourism Operation"""
    inner = f"""
    <!-- Central Hub -->
    <g transform="translate(300, 180)">
      <rect width="240" height="60" rx="10" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2.5"/>
      <text x="120" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">ECO-TOURISM PRINCIPLES</text>
      <text x="120" y="48" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Sustainable Operation</text>
    </g>

    <!-- 5 Operating Pillars -->
    <!-- 1. Walking Trails -->
    <g transform="translate(40, 60)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}"/>
      <text x="105" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">1. Pre-Marked Walking Trails</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Guided foot safaris prevent</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">off-road vehicle soil erosion</text>
    </g>

    <!-- 2. Distant Telescope Viewing -->
    <g transform="translate(590, 60)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="105" y="25" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">2. Distant Optical Viewing</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Using binoculars &amp; lenses</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">avoids stressing breeding herds</text>
    </g>

    <!-- 3. Low-Impact Tented Camps -->
    <g transform="translate(40, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_TEAL}"/>
      <text x="105" y="25" fill="{ACCENT_TEAL}" font-size="11" font-weight="700" text-anchor="middle">3. Low-Impact Tented Camps</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Solar power &amp; canvas structures</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">instead of heavy concrete hotels</text>
    </g>

    <!-- 4. Vehicle & Noise Caps -->
    <g transform="translate(315, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}"/>
      <text x="105" y="25" fill="{ACCENT_PURPLE}" font-size="11" font-weight="700" text-anchor="middle">4. Vehicle Fleet Regulation</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Capping vehicle numbers &amp;</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">mandating quiet electric drives</text>
    </g>

    <!-- 5. Zero-Waste Policy -->
    <g transform="translate(590, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_RED}"/>
      <text x="105" y="25" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">5. Strict Zero-Waste Audits</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Banning single-use plastics &amp;</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">preventing safari campfire litter</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="The Five Operational Pillars of Sustainable Eco-Tourism in Kenya")

def svg_push_pull_international_tourism():
    """SVG 10: Push-Pull Dynamics of International Tourism to Tropical Kenya"""
    inner = f"""
    <!-- Left: European/North American Winter Push Factors -->
    <g transform="translate(30, 65)">
      <rect width="360" height="340" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="180" y="28" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">TEMPERATE ORIGIN: PUSH FACTORS</text>
      
      <rect x="20" y="50" width="320" height="70" fill="{PANEL_BG_2}" rx="6"/>
      <text x="180" y="80" fill="{TEXT_MAIN}" font-size="12" font-weight="700" text-anchor="middle">Harsh Freezing Winter Conditions</text>
      <text x="180" y="100" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Sub-zero temperatures, snowstorms, short daylight</text>

      <g transform="translate(20, 140)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• High Disposable Income &amp; High Savings</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Generous Annual Paid Work Leave</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Strong Travel &amp; Vacation Culture</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Desire for Exotic African Wildlife Safari</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Direct International Airline Routes to Nairobi</text>
      </g>
    </g>

    <!-- Central Flow Arrows -->
    <path d="M 395,220 L 440,220" stroke="{ACCENT_GREEN}" stroke-width="4"/>
    <polygon points="435,213 448,220 435,227" fill="{ACCENT_GREEN}"/>

    <!-- Right: Kenyan Equatorial Pull Factors -->
    <g transform="translate(450, 65)">
      <rect width="360" height="340" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}" stroke-width="2"/>
      <text x="180" y="28" fill="{ACCENT_AMBER}" font-size="13" font-weight="700" text-anchor="middle">KENYA DESTINATION: PULL FACTORS</text>

      <rect x="20" y="50" width="320" height="70" fill="{PANEL_BG_2}" rx="6"/>
      <text x="180" y="80" fill="{ACCENT_AMBER}" font-size="12" font-weight="700" text-anchor="middle">Warm Equatorial Sunshine Year-Round</text>
      <text x="180" y="100" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Pristine white sandy beaches &amp; turquoise Indian Ocean</text>

      <g transform="translate(20, 140)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• The Big Five &amp; Great Wildebeest Migration</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Great Rift Valley Geysers, Lakes &amp; Mt. Kenya</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Authentic Cultural Heritage of 40+ Communities</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• UNESCO Historical Fort Jesus &amp; Gedi Ruins</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• World-Class Safari Lodges &amp; Utalii Hospitality</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Push-Pull Dynamics Governing International Tourism Inflows to Tropical Kenya")

def svg_thematic_map_kenya_attractions():
    """SVG 11: Thematic Map of Kenya: Spatial Distribution of Coastal vs Inland Tourist Hubs"""
    inner = f"""
    <!-- Kenya Map Vector Outline -->
    <g transform="translate(40, 60)">
      <path d="M 120,30 L 220,20 L 290,80 L 320,160 L 300,270 L 250,320 L 190,310 L 130,280 L 100,230 L 80,170 L 70,100 Z"
            fill="{PANEL_BG}" stroke="{BORDER_COLOR}" stroke-width="2"/>

      <!-- Coastal Circuit (Red Highlight along Coastline) -->
      <path d="M 250,320 L 300,270 L 320,160" fill="none" stroke="{ACCENT_RED}" stroke-width="6"/>
      <circle cx="260" cy="300" r="6" fill="{ACCENT_RED}"/>
      <text x="280" y="305" fill="{ACCENT_RED}" font-size="10" font-weight="700">Mombasa / Fort Jesus</text>

      <circle cx="285" cy="270" r="5" fill="{ACCENT_RED}"/>
      <text x="300" y="270" fill="{TEXT_MAIN}" font-size="9">Malindi / Gedi</text>

      <!-- Inland Circuit (Green Highlight) -->
      <!-- Maasai Mara -->
      <circle cx="110" cy="240" r="6" fill="{ACCENT_GREEN}"/>
      <text x="110" y="260" fill="{ACCENT_GREEN}" font-size="9.5" font-weight="700" text-anchor="middle">Maasai Mara</text>

      <!-- Amboseli & Kilimanjaro -->
      <circle cx="190" cy="280" r="5" fill="{ACCENT_GREEN}"/>
      <text x="190" y="298" fill="{TEXT_MAIN}" font-size="8.5" text-anchor="middle">Amboseli</text>

      <!-- Tsavo -->
      <circle cx="225" cy="265" r="5" fill="{ACCENT_GREEN}"/>
      <text x="225" y="255" fill="{TEXT_MAIN}" font-size="8.5" text-anchor="middle">Tsavo</text>

      <!-- Lake Nakuru & Bogoria -->
      <circle cx="130" cy="180" r="5" fill="{ACCENT_BLUE}"/>
      <text x="145" y="180" fill="{ACCENT_BLUE}" font-size="8.5">Nakuru / Bogoria</text>

      <!-- Mt. Kenya -->
      <polygon points="175,175 180,165 185,175" fill="{TEXT_MAIN}"/>
      <text x="180" y="160" fill="{TEXT_MAIN}" font-size="8.5" text-anchor="middle">Mt. Kenya</text>
    </g>

    <!-- Side Circuit Legend Panel -->
    <g transform="translate(420, 70)">
      <rect width="380" height="330" fill="{PANEL_BG}" rx="10" stroke="{BORDER_COLOR}"/>
      <text x="20" y="30" fill="{ACCENT_BLUE}" font-size="14" font-weight="700">Kenya's Dual Tourism Circuits</text>

      <text x="20" y="65" fill="{ACCENT_RED}" font-size="12" font-weight="700">1. Coastal Strip Circuit</text>
      <text x="20" y="85" fill="{TEXT_MUTED}" font-size="10.5">• Diani &amp; Watamu white sand coral beaches</text>
      <text x="20" y="103" fill="{TEXT_MUTED}" font-size="10.5">• UNESCO Fort Jesus (1593) &amp; Gedi Ruins</text>
      <text x="20" y="121" fill="{TEXT_MUTED}" font-size="10.5">• Marine parks (scuba, sport fishing) &amp; Kaya shrines</text>

      <text x="20" y="155" fill="{ACCENT_GREEN}" font-size="12" font-weight="700">2. Inland Wildlife &amp; Rift Circuit</text>
      <text x="20" y="175" fill="{TEXT_MUTED}" font-size="10.5">• Maasai Mara Great Wildebeest Migration</text>
      <text x="20" y="193" fill="{TEXT_MUTED}" font-size="10.5">• Tsavo &amp; Amboseli Big Five megafauna</text>
      <text x="20" y="211" fill="{TEXT_MUTED}" font-size="10.5">• Lake Bogoria geysers &amp; Lake Nakuru rhinos</text>
      <text x="20" y="229" fill="{TEXT_MUTED}" font-size="10.5">• Glacial peaks of Mt. Kenya &amp; prehistoric Kariandusi</text>

      <rect x="15" y="250" width="350" height="60" rx="6" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="25" y="272" fill="{ACCENT_AMBER}" font-size="11" font-weight="700">Transport Linkage:</text>
      <text x="25" y="292" fill="{TEXT_MAIN}" font-size="10">Connected by SGR Madaraka Express, Highway &amp; Flights</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Spatial Thematic Map of Kenya: Premier Coastal and Inland Tourism Circuits")

def svg_coastal_transect_ecosystems():
    """SVG 12: Transect of the Kenyan Coastal Strip: Coral Reefs, Beaches, Mangroves, and Kayas"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Cross Section Transect -->
      <!-- 1. Deep Ocean (Left) -->
      <rect x="0" y="140" width="120" height="190" fill="{ACCENT_BLUE}33"/>
      <text x="60" y="200" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">Indian Ocean</text>
      <text x="60" y="220" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Deep Waters</text>

      <!-- 2. Barrier Coral Reef -->
      <polygon points="120,170 150,110 180,170" fill="{ACCENT_AMBER}" stroke="{BORDER_COLOR}"/>
      <text x="150" y="100" fill="{ACCENT_AMBER}" font-size="10" font-weight="700" text-anchor="middle">Coral Reef</text>

      <!-- 3. Calm Turquoise Lagoon -->
      <polygon points="180,170 340,170 340,240 180,240" fill="{ACCENT_TEAL}44"/>
      <text x="260" y="195" fill="{ACCENT_TEAL}" font-size="11" font-weight="700" text-anchor="middle">Calm Shallow Lagoon</text>
      <text x="260" y="215" fill="{TEXT_MAIN}" font-size="9" text-anchor="middle">(Swimming &amp; Glass-Bottom Boats)</text>

      <!-- 4. White Sandy Beach -->
      <path d="M 340,170 L 440,170 L 470,220 L 340,220 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}"/>
      <text x="390" y="160" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">White Sand Beach</text>
      <text x="390" y="180" fill="{ACCENT_AMBER}" font-size="9" text-anchor="middle">(Diani / Watamu)</text>

      <!-- 5. Mangrove Creek Estuary -->
      <rect x="440" y="170" width="120" height="70" fill="{ACCENT_GREEN}33"/>
      <text x="500" y="195" fill="{ACCENT_GREEN}" font-size="10" font-weight="700" text-anchor="middle">Mangrove Estuary</text>
      <text x="500" y="215" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Tidal Swamp &amp; Birds</text>

      <!-- 6. Sacred Kaya Indigenous Forest (Right) -->
      <path d="M 560,170 L 740,110 L 740,330 L 560,330 Z" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="650" y="145" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">Sacred Kaya Forest</text>
      <text x="650" y="165" fill="{TEXT_MAIN}" font-size="10" text-anchor="middle">Mijikenda Shrines (UNESCO)</text>
      <text x="650" y="185" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Ancient indigenous flora</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Transect of Kenyan Coastal Ecosystems: Barrier Reefs to Sacred Kaya Forests")

def svg_economic_multiplier_tourism():
    """SVG 13: Economic Multiplier Effect of Tourism in Kenya"""
    inner = f"""
    <!-- Central Spending Trigger -->
    <g transform="translate(300, 60)">
      <rect width="240" height="60" rx="8" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2.5"/>
      <text x="120" y="26" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">INTERNATIONAL TOURIST INFLOW</text>
      <text x="120" y="46" fill="{TEXT_MAIN}" font-size="11" font-weight="600" text-anchor="middle">Foreign Currency Expenditure</text>
    </g>

    <!-- 4 Multiplier Channels -->
    <!-- 1. Hospitality & Aviation -->
    <g transform="translate(40, 160)">
      <rect width="170" height="210" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}"/>
      <text x="85" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">1. Hospitality &amp; Air</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10">• Hotel bed nights</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10">• Safari van hires</text>
      <text x="15" y="95" fill="{TEXT_MAIN}" font-size="10">• Aviation landing fees</text>
      <text x="15" y="125" fill="{ACCENT_BLUE}" font-size="10" font-weight="600">Direct Jobs:</text>
      <text x="15" y="145" fill="{TEXT_MUTED}" font-size="9">Chefs, guides, drivers,</text>
      <text x="15" y="160" fill="{TEXT_MUTED}" font-size="9">rangers, flight crew</text>
    </g>

    <!-- 2. Agriculture & Farming -->
    <g transform="translate(230, 160)">
      <rect width="170" height="210" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}"/>
      <text x="85" y="25" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">2. Local Agriculture</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10">• Fresh vegetables</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10">• Tropical fruits</text>
      <text x="15" y="95" fill="{TEXT_MAIN}" font-size="10">• Dairy &amp; meat supply</text>
      <text x="15" y="125" fill="{ACCENT_GREEN}" font-size="10" font-weight="600">Rural Linkage:</text>
      <text x="15" y="145" fill="{TEXT_MUTED}" font-size="9">Direct guaranteed market</text>
      <text x="15" y="160" fill="{TEXT_MUTED}" font-size="9">for smallholder farmers</text>
    </g>

    <!-- 3. Jua Kali Cottage Crafts -->
    <g transform="translate(420, 160)">
      <rect width="170" height="210" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="85" y="25" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">3. Jua Kali Crafts</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10">• Sisal Ciondo baskets</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10">• Kisii soapstone</text>
      <text x="15" y="95" fill="{TEXT_MAIN}" font-size="10">• Maasai beadwork</text>
      <text x="15" y="125" fill="{ACCENT_AMBER}" font-size="10" font-weight="600">Artisan Income:</text>
      <text x="15" y="145" fill="{TEXT_MUTED}" font-size="9">Direct cash earnings</text>
      <text x="15" y="160" fill="{TEXT_MUTED}" font-size="9">for women &amp; youths</text>
    </g>

    <!-- 4. Public Infrastructure & Taxes -->
    <g transform="translate(610, 160)">
      <rect width="190" height="210" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}"/>
      <text x="95" y="25" fill="{ACCENT_PURPLE}" font-size="11" font-weight="700" text-anchor="middle">4. State Revenue &amp; Roads</text>
      <text x="15" y="55" fill="{TEXT_MAIN}" font-size="10">• VAT &amp; park entry fees</text>
      <text x="15" y="75" fill="{TEXT_MAIN}" font-size="10">• Foreign exchange balance</text>
      <text x="15" y="95" fill="{TEXT_MAIN}" font-size="10">• ASAL tarmac roads</text>
      <text x="15" y="125" fill="{ACCENT_PURPLE}" font-size="10" font-weight="600">National Impact:</text>
      <text x="15" y="145" fill="{TEXT_MUTED}" font-size="9">Funds public services,</text>
      <text x="15" y="160" fill="{TEXT_MUTED}" font-size="9">schools &amp; healthcare</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="The Tourism Economic Multiplier Effect Across Kenya's Productive Sectors")

def svg_swiss_alpine_infrastructure():
    """SVG 14: Physical and Technological Infrastructure of Swiss Alpine Tourism"""
    inner = f"""
    <g transform="translate(40, 65)">
      <!-- Alpine Glaciated Mountain Profile -->
      <path d="M 20,330 L 180,180 L 320,60 L 480,190 L 740,330 Z" fill="{PANEL_BG_2}" stroke="{BORDER_COLOR}" stroke-width="2"/>
      <!-- Snow Cap on Peak -->
      <polygon points="300,80 320,60 340,80" fill="{TEXT_MAIN}"/>
      <text x="320" y="45" fill="{TEXT_MAIN}" font-size="12" font-weight="700" text-anchor="middle">Matterhorn / Alpine Glaciated Peak (>4,000m)</text>

      <!-- Electrified Cogwheel Railway (Left Slope) -->
      <line x1="80" y1="280" x2="260" y2="120" stroke="{ACCENT_RED}" stroke-width="4"/>
      <text x="140" y="180" fill="{ACCENT_RED}" font-size="11" font-weight="700" transform="rotate(-40, 140, 180)">Electrified Cogwheel Railway</text>

      <!-- High-Altitude Aerial Cable Car (Right Slope) -->
      <line x1="320" y1="80" x2="620" y2="240" stroke="{ACCENT_BLUE}" stroke-width="2.5" stroke-dasharray="6,4"/>
      <rect x="460" y="150" width="30" height="20" rx="4" fill="{ACCENT_BLUE}"/>
      <text x="475" y="140" fill="{ACCENT_BLUE}" font-size="10" font-weight="700" text-anchor="middle">Cable Car</text>

      <!-- Winter Ski Slopes & Summer Hiking Trails -->
      <rect x="480" y="240" width="220" height="70" rx="6" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}"/>
      <text x="590" y="265" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">Dual-Season Alpine Recreation</text>
      <text x="590" y="285" fill="{TEXT_MAIN}" font-size="10" text-anchor="middle">Winter: World-Class Skiing &amp; Skating</text>
      <text x="590" y="300" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Summer: High-Altitude Mountaineering</text>

      <!-- Thermal Spa at Base (Left) -->
      <rect x="30" y="270" width="160" height="50" rx="6" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="110" y="292" fill="{ACCENT_AMBER}" font-size="10" font-weight="700" text-anchor="middle">Thermal Mineral Spas</text>
      <text x="110" y="308" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">(St. Moritz / Baden)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Technological and Physical Infrastructure of Swiss Alpine Tourism")

def svg_kenya_vs_switzerland_matrix():
    """SVG 15: Comparative Matrix: Kenya Tropical Savanna vs Switzerland Alpine Ecosystems"""
    inner = f"""
    <!-- Left: Kenya Fishery Model -->
    <g transform="translate(30, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}" stroke-width="2"/>
      <text x="185" y="28" fill="{ACCENT_GREEN}" font-size="13" font-weight="700" text-anchor="middle">KENYA TOURISM MODEL</text>
      
      <rect x="20" y="50" width="330" height="85" fill="{PANEL_BG_2}" rx="6"/>
      <text x="185" y="75" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">Tropical Savanna &amp; Coastal Marine Hub</text>
      <text x="185" y="95" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Warm equatorial sunshine throughout the year</text>
      <text x="185" y="115" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Free-ranging Big Five megafauna in open game parks</text>

      <g transform="translate(20, 155)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• Marine Attractions: Pristine coral beaches &amp; reefs</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Culture: 40+ distinct ethnic groups &amp; traditions</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Transit: Highways, SGR, safari vans, bush flights</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Domestic Tourism: Low (income &amp; tariff constraints)</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Seasonality: Off-peak drops in April and October</text>
      </g>
    </g>

    <!-- Right: Switzerland Fishery Model -->
    <g transform="translate(440, 65)">
      <rect width="370" height="340" rx="10" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}" stroke-width="2"/>
      <text x="185" y="28" fill="{ACCENT_BLUE}" font-size="13" font-weight="700" text-anchor="middle">SWITZERLAND TOURISM MODEL</text>
      
      <rect x="20" y="50" width="330" height="85" fill="{PANEL_BG_2}" rx="6"/>
      <text x="185" y="75" fill="{ACCENT_BLUE}" font-size="12" font-weight="700" text-anchor="middle">Central European Alpine Superpower</text>
      <text x="185" y="95" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Landlocked nation; 60% covered by glaciated Alps</text>
      <text x="185" y="115" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">Dual-season: summer hiking vs winter snow skiing</text>

      <g transform="translate(20, 155)">
        <text x="0" y="20" fill="{TEXT_MAIN}" font-size="10.5">• Marine Attractions: NONE (Landlocked nation)</text>
        <text x="0" y="45" fill="{TEXT_MAIN}" font-size="10.5">• Wildlife: Kept in zoos; sparse native alpine fauna</text>
        <text x="0" y="70" fill="{TEXT_MAIN}" font-size="10.5">• Transit: Multi-billion electrified cog rails &amp; cable cars</text>
        <text x="0" y="95" fill="{TEXT_MAIN}" font-size="10.5">• Domestic Tourism: Massive (high citizen savings)</text>
        <text x="0" y="120" fill="{TEXT_MAIN}" font-size="10.5">• Seasonality: Continuous 12-month year-round revenue</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Comparative Matrix: Kenya Tropical Savanna vs Switzerland Alpine Ecosystems")

def svg_six_point_expansion_plan():
    """SVG 16: Six-Point Strategic Action Plan for Kenyan Tourism Sector Expansion"""
    inner = f"""
    <!-- Central Strategic Hub -->
    <g transform="translate(280, 190)">
      <rect width="280" height="60" rx="10" fill="{PANEL_BG_2}" stroke="{ACCENT_GREEN}" stroke-width="2.5"/>
      <text x="140" y="28" fill="{ACCENT_GREEN}" font-size="12" font-weight="700" text-anchor="middle">KENYA TOURISM SECTOR</text>
      <text x="140" y="48" fill="{TEXT_MAIN}" font-size="11" font-weight="700" text-anchor="middle">STRATEGIC EXPANSION PLAN</text>
    </g>

    <!-- 6 Strategic Pillars -->
    <!-- 1. ASAL Roads & Airstrips -->
    <g transform="translate(40, 70)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_RED}"/>
      <text x="105" y="25" fill="{ACCENT_RED}" font-size="11" font-weight="700" text-anchor="middle">1. ASAL Infrastructure</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Tarmacking remote northern roads</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">to open new game circuits</text>
    </g>

    <!-- 2. KTB Global Marketing -->
    <g transform="translate(315, 60)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_AMBER}"/>
      <text x="105" y="25" fill="{ACCENT_AMBER}" font-size="11" font-weight="700" text-anchor="middle">2. KTB Global Marketing</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Aggressive campaigns in Asia,</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Middle East &amp; Eastern Europe</text>
    </g>

    <!-- 3. Domestic Off-Peak Subsidies -->
    <g transform="translate(590, 70)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_BLUE}"/>
      <text x="105" y="25" fill="{ACCENT_BLUE}" font-size="11" font-weight="700" text-anchor="middle">3. Domestic Subsidies</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Discounted hotel packages to</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">cushion April/October off-peak</text>
    </g>

    <!-- 4. Tourist Police Security -->
    <g transform="translate(40, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_PURPLE}"/>
      <text x="105" y="25" fill="{ACCENT_PURPLE}" font-size="11" font-weight="700" text-anchor="middle">4. Security Reinforcement</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Deploying Tourist Police Units</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">along coastal beaches &amp; parks</text>
    </g>

    <!-- 5. Tax & Tariff Incentives -->
    <g transform="translate(315, 310)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_TEAL}"/>
      <text x="105" y="25" fill="{ACCENT_TEAL}" font-size="11" font-weight="700" text-anchor="middle">5. Tariff &amp; Tax Relief</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Lowering hotel VAT &amp; park fees</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">to ensure global cost competition</text>
    </g>

    <!-- 6. Product Diversification -->
    <g transform="translate(590, 300)">
      <rect width="210" height="70" rx="8" fill="{PANEL_BG}" stroke="{ACCENT_GREEN}"/>
      <text x="105" y="25" fill="{ACCENT_GREEN}" font-size="11" font-weight="700" text-anchor="middle">6. Product Diversification</text>
      <text x="105" y="45" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">Expanding cultural, conference</text>
      <text x="105" y="60" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">(MICE), sports &amp; agro-tourism</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=440, title="Six-Point Strategic Action Plan for Kenyan Tourism Sector Expansion")


# =============================================================================
# ENRICHMENT PIPELINE
# =============================================================================

def run_enrichment():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 3: Visual Enrichment Engine")
    print("Attaching 16 Vector SVGs & 6 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    topic = Topic.objects.filter(name="Wildlife and Tourism").first()
    if not topic:
        print("[!] Error: Topic 3 'Wildlife and Tourism' not found. Run ingest_form4_geography_topic3.py first.")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    if len(lessons) < 6:
        print(f"[!] Warning: Found {len(lessons)} lessons (expected 6).")

    lesson_1 = lessons[0]  # Foundations & Factors
    lesson_2 = lessons[1]  # Protected Area Systems
    lesson_3 = lessons[2]  # Significance, Threats & Management
    lesson_4 = lessons[3]  # Tourism Concepts & Factors
    lesson_5 = lessons[4]  # Coastal & Inland Attractions
    lesson_6 = lessons[5]  # Comparative Analysis & Expansion

    # Clear existing LessonAssets for clean enrichment
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean enrichment.")

    # -------------------------------------------------------------------------
    # LESSON 1 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 1: {lesson_1.title}")
    attach_svg_to_block(lesson_1, "Ecological Factor Web of East African Wildlife Distribution", svg_ecological_factor_web)
    attach_svg_to_block(lesson_1, "Relief and Aspect Profile: Windward Forest vs Leeward Rain-Shadow Savanna", svg_windward_leeward_profile)
    attach_wikimedia_to_block(
        lesson=lesson_1,
        exact_title="Thomson's Gazelle in the Open Savanna Plains of Amboseli National Park",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Gacela_de_Thomson_%28Eudorcas_thomsonii%29%2C_parque_nacional_de_Amboseli%2C_Kenia%2C_2024-05-23%2C_DD_11.jpg",
        author="Diego Delso, Wikimedia Commons",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Gacela_de_Thomson_(Eudorcas_thomsonii),_parque_nacional_de_Amboseli,_Kenia,_2024-05-23,_DD_11.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 2 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 2: {lesson_2.title}")
    attach_svg_to_block(lesson_2, "Classification Hierarchy of Protected Areas (Parks, Reserves, Sanctuaries)", svg_protected_areas_taxonomy)
    attach_svg_to_block(lesson_2, "Zonation and Land-Use Boundaries of a National Park vs Game Reserve", svg_park_vs_reserve_zonation)
    attach_svg_to_block(lesson_2, "Specialized Sanctuary Architecture & Captive Breeding Cycle", svg_sanctuary_architecture_breeding)
    attach_wikimedia_to_block(
        lesson=lesson_2,
        exact_title="Endangered Black Rhinoceros in Lake Nakuru Protected Sanctuary",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/6/6e/Black_Rhino_%28Diceros_bicornis%29_%288290870387%29.jpg",
        author="Bernard DUPONT, Wikimedia Commons",
        licensing="CC BY-SA 2.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Black_Rhino_(Diceros_bicornis)_(8290870387).jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 3 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 3: {lesson_3.title}")
    attach_svg_to_block(lesson_3, "Threat Matrix: Human-Induced vs Natural Pressures on East African Wildlife", svg_threat_matrix_dual_column)
    attach_svg_to_block(lesson_3, "The KWS Wildlife Management vs Conservation Strategic Framework", svg_management_vs_conservation_framework)
    attach_svg_to_block(lesson_3, "Step-by-Step Logistics of KWS Animal Translocation Process", svg_translocation_logistics)
    attach_wikimedia_to_block(
        lesson=lesson_3,
        exact_title="Kenya Wildlife Service (KWS) Ranger Briefing and Conservation Patrols",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Press_listen_to_KWS_Ranger_Simon_Gitau_on_Mount_Kenya_climbing_tips.jpg",
        author="Ronald Robert, Wikimedia Commons",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Press_listen_to_KWS_Ranger_Simon_Gitau_on_Mount_Kenya_climbing_tips.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 4 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 4: {lesson_4.title}")
    attach_svg_to_block(lesson_4, "The Five Pillars of Eco-Tourism Operation", svg_ecotourism_five_pillars)
    attach_svg_to_block(lesson_4, "Push-Pull Dynamics of International Tourism to Tropical Kenya", svg_push_pull_international_tourism)
    attach_wikimedia_to_block(
        lesson=lesson_4,
        exact_title="Historical Fort Jesus Built in 1593 in Coastal Mombasa",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Fort_Jesus%2C_Mombasa1.jpg",
        author="Chris huh, Wikimedia Commons",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Fort_Jesus,_Mombasa1.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 5 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 5: {lesson_5.title}")
    attach_svg_to_block(lesson_5, "Thematic Map of Kenya: Spatial Distribution of Coastal vs Inland Tourist Hubs", svg_thematic_map_kenya_attractions)
    attach_svg_to_block(lesson_5, "Transect of the Kenyan Coastal Strip: Coral Reefs, Beaches, Mangroves, and Kayas", svg_coastal_transect_ecosystems)
    attach_svg_to_block(lesson_5, "Economic Multiplier Effect of Tourism in Kenya", svg_economic_multiplier_tourism)
    attach_wikimedia_to_block(
        lesson=lesson_5,
        exact_title="The Great Wildebeest Migration in Maasai Mara Game Reserve",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/7/7b/Maasai_Mara_Wildebeest_Migrations.jpg",
        author="Kidoleeee, Wikimedia Commons",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Maasai_Mara_Wildebeest_Migrations.jpg"
    )

    # -------------------------------------------------------------------------
    # LESSON 6 ENRICHMENT
    # -------------------------------------------------------------------------
    print(f"\n[*] Enriching Lesson 6: {lesson_6.title}")
    attach_svg_to_block(lesson_6, "Physical and Technological Infrastructure of Swiss Alpine Tourism", svg_swiss_alpine_infrastructure)
    attach_svg_to_block(lesson_6, "Comparative Matrix: Kenya Tropical Savanna vs Switzerland Alpine Ecosystems", svg_kenya_vs_switzerland_matrix)
    attach_svg_to_block(lesson_6, "Six-Point Strategic Action Plan for Kenyan Tourism Sector Expansion", svg_six_point_expansion_plan)
    attach_wikimedia_to_block(
        lesson=lesson_6,
        exact_title="Modern Electrified Cable Car Transit Ascending the Swiss Alps with Matterhorn View",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/f/f7/Cable_car_and_Matterhorn.jpg",
        author="Tiia Monto, Wikimedia Commons",
        licensing="CC BY-SA 3.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Cable_car_and_Matterhorn.jpg"
    )

    print("\n" + "=" * 80)
    print("[SUCCESS] Form 4 Geography Topic 3 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {LessonAsset.objects.filter(lesson__in=lessons).count()}")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment()
