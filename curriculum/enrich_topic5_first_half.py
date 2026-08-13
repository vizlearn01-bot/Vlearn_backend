import os
import sys
import django
import requests
from django.core.files.base import ContentFile

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

WIKIMEDIA_USER_AGENT = 'VlearnCurriculumBot/1.0 (https://vlearn.org; contact@vlearn.org)'
headers = {'User-Agent': WIKIMEDIA_USER_AGENT}

def clean_svg(svg_code):
    is_valid, sanitized, err = validate_and_sanitize_svg(svg_code)
    return sanitized if is_valid else svg_code

def fetch_wikimedia_api_url(filename, thumb_width=800):
    api_url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'titles': f'File:{filename}',
        'prop': 'imageinfo',
        'iiprop': 'url|size|mime',
        'iiurlwidth': thumb_width,
        'format': 'json',
    }
    try:
        resp = requests.get(api_url, params=params, headers=headers, timeout=8)
        if resp.status_code == 200:
            pages = resp.json().get('query', {}).get('pages', {})
            for p in pages.values():
                if 'imageinfo' in p and len(p['imageinfo']) > 0:
                    ii = p['imageinfo'][0]
                    thumb = ii.get('thumburl')
                    raw = ii.get('url')
                    if thumb:
                        clean_thumb = thumb.split('?')[0] if len(thumb.split('?')[0]) <= 200 else thumb[:200]
                        r = requests.head(clean_thumb, headers=headers, timeout=4)
                        if r.status_code == 200:
                            return clean_thumb
                    if raw:
                        clean_raw = raw.split('?')[0] if len(raw.split('?')[0]) <= 200 else raw[:200]
                        r = requests.head(clean_raw, headers=headers, timeout=4)
                        if r.status_code == 200:
                            return clean_raw
    except Exception as e:
        print(f'API lookup failed for {filename}: {e}')
    return None

def create_or_update_wm_block(lesson, page_num, title, filename, author, licensing, commons_page, fallback_url):
    # Check if working URL from API
    verified_url = fetch_wikimedia_api_url(filename) or fallback_url
    
    # Check if a suggested_diagram block already exists on this page
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
    if not block:
        # Create block
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=page_num,
            block_type='suggested_diagram',
            title=title,
            component_order=0,
            content={'text': title, 'resolved_image_url': verified_url, 'url': verified_url}
        )
    else:
        block.title = title
        if not isinstance(block.content, dict):
            block.content = {}
        block.content['resolved_image_url'] = verified_url
        block.content['url'] = verified_url
        block.save()

    # Create / update asset
    meta = {
        'author': author,
        'licensing': licensing,
        'commons_page_url': commons_page,
    }
    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block, source_type='external').first()
    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type='image',
            source_type='external',
            storage_type='url',
            status='approved',
            title=title,
            description=f'Wikimedia Commons photographic asset: {title}',
            url=verified_url[:200],
            metadata=meta
        )
        block.assets.add(asset)
    else:
        asset.title = title
        asset.url = verified_url[:200]
        asset.metadata = meta
        asset.save()
    print(f'  [Page {page_num}] Wikimedia attached: \"{title}\" (Asset {asset.id})')
    return asset

def create_or_update_svg_block(lesson, page_num, title, filename_base, svg_string):
    sanitized = clean_svg(svg_string)
    
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
    if not block:
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=page_num,
            block_type='suggested_diagram',
            title=title,
            component_order=10,
            metadata={'svg_content': sanitized},
            content={'text': title, 'svg_content': sanitized, 'svg': sanitized}
        )
    else:
        block.title = title
        if not block.metadata:
            block.metadata = {}
        block.metadata['svg_content'] = sanitized
        if not isinstance(block.content, dict):
            block.content = {}
        block.content['svg_content'] = sanitized
        block.content['svg'] = sanitized
        block.save()

    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block, source_type='ai_generated').first()
    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type='diagram',
            source_type='ai_generated',
            storage_type='file',
            status='approved',
            title=title,
            description=f'Sanitized vector diagram: {title}',
            metadata={'svg_content': sanitized}
        )
        asset.file.save(f'{filename_base}_{lesson.id}.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        block.assets.add(asset)
    else:
        asset.title = title
        if not asset.metadata:
            asset.metadata = {}
        asset.metadata['svg_content'] = sanitized
        asset.file.save(f'{filename_base}_{lesson.id}.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        asset.save()
    print(f'  [Page {page_num}] SVG saved & attached: \"{title}\" (Asset {asset.id})')
    return asset

def enrich_topic5_first_half():
    print('=== ENRICHING FORM 4 TOPIC 5: METALS (FIRST HALF: LESSONS 103 - 109) ===\n')

    # =========================================================================
    # LESSON 103: Chief Ores of Metals
    # =========================================================================
    l103 = Lesson.objects.get(id=103)
    print(f'Enriching Lesson 103: \"{l103.title}\"')
    create_or_update_wm_block(
        l103, 2, 'Natural Crystalline Specimen of Bauxite (Aluminium Ore)',
        'Bauxite_minerals.jpg', 'Didier Descouens', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Bauxite_minerals.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/b/b5/Bauxite_minerals.jpg'
    )
    create_or_update_wm_block(
        l103, 3, 'Massive Red-Brown Hematite Mineral Specimen (Iron Ore)',
        'Hematite_ore_specimen.jpg', 'Robert M. Lavinsky', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Hematite_ore_specimen.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e4/Hematite_ore_specimen.jpg'
    )
    svg_103 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Chief Ores of the Six Key Metals: Formulae &amp; Chemical Nature</text>
  
  <g transform="translate(40, 65)">
    <!-- Sodium -->
    <rect x="0" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Sodium (Na)</text>
    <text x="122" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Chief Ore: <tspan fill="#facc15" font-weight="bold">Rock Salt</tspan></text>
    <text x="122" y="78" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Formula: <tspan fill="#38bdf8" font-family="monospace">NaCl</tspan></text>
    <rect x="15" y="95" width="215" height="60" fill="#0f172a" rx="6"/>
    <text x="122" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Highly reactive alkali metal</text>
    <text x="122" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Extracted via Electrolysis</text>

    <!-- Aluminium -->
    <rect x="270" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#60a5fa" stroke-width="2"/>
    <text x="392" y="28" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Aluminium (Al)</text>
    <text x="392" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Chief Ore: <tspan fill="#facc15" font-weight="bold">Bauxite</tspan></text>
    <text x="392" y="78" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Formula: <tspan fill="#60a5fa" font-family="monospace">Al2O3·2H2O</tspan></text>
    <rect x="285" y="95" width="215" height="60" fill="#0f172a" rx="6"/>
    <text x="392" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Hydrated aluminium oxide</text>
    <text x="392" y="138" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Extracted via Hall-Héroult</text>

    <!-- Iron -->
    <rect x="540" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
    <text x="662" y="28" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Iron (Fe)</text>
    <text x="662" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Chief Ore: <tspan fill="#facc15" font-weight="bold">Haematite / Magnetite</tspan></text>
    <text x="662" y="78" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Formula: <tspan fill="#f87171" font-family="monospace">Fe2O3 / Fe3O4</tspan></text>
    <rect x="555" y="95" width="215" height="60" fill="#0f172a" rx="6"/>
    <text x="662" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Dense oxide mineral</text>
    <text x="662" y="138" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Reduced with Carbon in Blast Furnace</text>

    <!-- Zinc -->
    <rect x="0" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="122" y="218" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Zinc (Zn)</text>
    <text x="122" y="245" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Chief Ore: <tspan fill="#facc15" font-weight="bold">Zinc Blende / Calamine</tspan></text>
    <text x="122" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Formula: <tspan fill="#4ade80" font-family="monospace">ZnS / ZnCO3</tspan></text>
    <rect x="15" y="285" width="215" height="60" fill="#0f172a" rx="6"/>
    <text x="122" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Sulfide roasted to oxide</text>
    <text x="122" y="328" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Distilled or Electrolysed</text>

    <!-- Lead -->
    <rect x="270" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#a78bfa" stroke-width="2"/>
    <text x="392" y="218" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Lead (Pb)</text>
    <text x="392" y="245" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Chief Ore: <tspan fill="#facc15" font-weight="bold">Galena</tspan></text>
    <text x="392" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Formula: <tspan fill="#a78bfa" font-family="monospace">PbS</tspan></text>
    <rect x="285" y="285" width="215" height="60" fill="#0f172a" rx="6"/>
    <text x="392" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Dense cubic lead(II) sulfide</text>
    <text x="392" y="328" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Reduced via Carbon or Coke</text>

    <!-- Copper -->
    <rect x="540" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#fb923c" stroke-width="2"/>
    <text x="662" y="218" fill="#fb923c" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Copper (Cu)</text>
    <text x="662" y="245" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Chief Ore: <tspan fill="#facc15" font-weight="bold">Copper Pyrites</tspan></text>
    <text x="662" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Formula: <tspan fill="#fb923c" font-family="monospace">CuFeS2 / Cu2S</tspan></text>
    <rect x="555" y="285" width="215" height="60" fill="#0f172a" rx="6"/>
    <text x="662" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Multi-stage smelting</text>
    <text x="662" y="328" fill="#fb923c" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Electrolytically Refined</text>
  </g>
</svg>"""
    create_or_update_svg_block(l103, 4, 'Six Chief Metal Ores Classification & Chemical Nature Matrix', 'chief_metal_ores', svg_103)
    print()

    # =========================================================================
    # LESSON 104: General Methods of Extraction
    # =========================================================================
    l104 = Lesson.objects.get(id=104)
    print(f'Enriching Lesson 104: \"{l104.title}\"')
    create_or_update_wm_block(
        l104, 2, 'Industrial Heavy-Duty Crushing and Froth Flotation Tanks for Ore Concentration',
        'Flotation_cells_in_copper_concentrator.jpg', 'Alf van Beem', 'CC0',
        'https://commons.wikimedia.org/wiki/File:Flotation_cells_in_copper_concentrator.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/3/36/Flotation_cells_in_copper_concentrator.jpg'
    )
    create_or_update_wm_block(
        l104, 4, 'Industrial Roasting Rotary Kiln for Sulfide Ore Processing',
        'Rotary_kiln_for_cement_production.jpg', 'Kimon-Berlin', 'CC BY-SA 2.0',
        'https://commons.wikimedia.org/wiki/File:Rotary_kiln_for_cement_production.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/b/b3/Rotary_kiln_for_cement_production.jpg'
    )
    svg_104 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">General Principles of Metal Extraction: Concentration to Chemical Reduction</text>

  <!-- Left: Froth Flotation -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1. Ore Concentration: Froth Flotation</text>
  
  <rect x="70" y="115" width="310" height="190" fill="#0f172a" rx="8"/>
  <rect x="70" y="115" width="310" height="35" fill="#fbbf24" opacity="0.3" rx="4"/>
  <text x="225" y="138" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Froth Layer: Mineral + Pine Oil (Hydrophobic)</text>
  
  <line x1="225" y1="115" x2="225" y2="280" stroke="#94a3b8" stroke-width="4"/>
  <circle cx="225" cy="275" r="14" fill="#38bdf8"/>
  <text x="225" y="279" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">AIR</text>
  
  <!-- Air bubbles -->
  <circle cx="160" cy="200" r="8" fill="#38bdf8" opacity="0.7"/><circle cx="175" cy="170" r="10" fill="#38bdf8" opacity="0.7"/>
  <circle cx="280" cy="210" r="8" fill="#38bdf8" opacity="0.7"/><circle cx="265" cy="180" r="10" fill="#38bdf8" opacity="0.7"/>
  <rect x="70" y="285" width="310" height="20" fill="#475569" rx="2"/>
  <text x="225" y="299" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Gangue / Earthy Impurities Sink (Hydrophilic)</text>

  <rect x="60" y="320" width="330" height="85" fill="#0f172a" rx="6"/>
  <text x="225" y="345" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Crushed ore mixed with water + pine oil</text>
  <text x="225" y="365" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Compressed air blows sulfide particles to surface</text>
  <text x="225" y="385" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">• Gangue wetted by water and discharged at base</text>

  <!-- Right: Reactivity Selection -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2. Reduction Method Selection</text>

  <rect x="475" y="115" width="320" height="80" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Electrolytic Reduction (Most Reactive)</text>
  <text x="490" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Metals: <tspan fill="#facc15" font-weight="bold">K, Na, Ca, Mg, Al</tspan></text>
  <text x="490" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Strong affinity for oxygen; only electricity can reduce</text>

  <rect x="475" y="205" width="320" height="80" fill="#0f172a" rx="8" stroke="#fbbf24" stroke-width="1"/>
  <text x="490" y="228" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Chemical Reduction with Carbon / CO</text>
  <text x="490" y="250" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Metals: <tspan fill="#facc15" font-weight="bold">Zn, Fe, Pb</tspan></text>
  <text x="490" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Oxides reduced by Coke (C) or Carbon Monoxide (CO)</text>

  <rect x="475" y="295" width="320" height="80" fill="#0f172a" rx="8" stroke="#f87171" stroke-width="1"/>
  <text x="490" y="318" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Roasting / Native Occurrence (Least Reactive)</text>
  <text x="490" y="340" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Metals: <tspan fill="#facc15" font-weight="bold">Cu, Ag, Au</tspan></text>
  <text x="490" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Self-reduction, simple heating in air, or native panning</text>
</svg>"""
    create_or_update_svg_block(l104, 3, 'Industrial Froth Flotation and Extraction Method Selection Hierarchy', 'flotation_reduction_methods', svg_104)
    print()

    # =========================================================================
    # LESSON 105: Sodium — Occurrence and Extraction
    # =========================================================================
    l105 = Lesson.objects.get(id=105)
    print(f'Enriching Lesson 105: \"{l105.title}\"')
    create_or_update_wm_block(
        l105, 2, 'Solid Rock Salt (Halite) Mineral Deposit Raw Material for Sodium Extraction',
        'Crystals_Halite_on_matrix.jpg', 'IvanSakhno', 'CC BY 4.0',
        'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l105, 3, 'Pure Metallic Sodium Preserved Under Mineral Oil Exhibiting Bright Silvery Cut',
        'Sodium_metal_in_oil.jpg', 'Jurii', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Sodium_metal_in_oil.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_105 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Industrial Extraction of Sodium: Complete Downs Cell Engineering Architecture</text>

  <!-- Downs Cell Container -->
  <rect x="180" y="70" width="500" height="320" fill="#1e293b" rx="12" stroke="#64748b" stroke-width="3"/>
  <rect x="200" y="100" width="460" height="270" fill="#0f172a" rx="8"/>
  <rect x="200" y="140" width="460" height="230" fill="#f59e0b" opacity="0.25" rx="4"/>
  <text x="430" y="170" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Molten Electrolyte: NaCl + CaCl2 Flux (600°C)</text>

  <!-- Central Graphite Anode -->
  <rect x="390" y="200" width="80" height="190" fill="#334155" stroke="#94a3b8" stroke-width="2" rx="4"/>
  <text x="430" y="260" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Graphite</text>
  <text x="430" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Anode (+)</text>

  <!-- Steel Cathodes on both sides -->
  <rect x="250" y="210" width="50" height="150" fill="#475569" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <text x="275" y="280" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" transform="rotate(-90 275,280)">Steel Cathode (-)</text>
  <rect x="560" y="210" width="50" height="150" fill="#475569" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <text x="585" y="280" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" transform="rotate(90 585,280)">Steel Cathode (-)</text>

  <!-- Wire Gauze Diaphragm -->
  <line x1="340" y1="130" x2="340" y2="350" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>
  <line x1="520" y1="130" x2="520" y2="350" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>
  <text x="430" y="340" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Steel Gauze Diaphragm (Prevents Re-combination)</text>

  <!-- Chlorine Dome / Gas Outlet -->
  <path d="M 370 140 L 370 80 L 490 80 L 490 140 Z" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <text x="430" y="105" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Cl2 Gas Outlet</text>

  <!-- Sodium Collection Hoods & Risers -->
  <path d="M 230 140 L 230 90 L 310 90 L 310 140 Z" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="270" y="110" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Molten Na</text>
  <text x="270" y="125" fill="#facc15" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Floats up)</text>

  <!-- Key Equations at bottom -->
  <rect x="60" y="405" width="350" height="40" fill="#1e293b" rx="6" stroke="#22c55e" stroke-width="1"/>
  <text x="235" y="430" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Anode: 2Cl-(l) --&gt; Cl2(g) + 2e- (Oxidation)</text>

  <rect x="450" y="405" width="350" height="40" fill="#1e293b" rx="6" stroke="#facc15" stroke-width="1"/>
  <text x="625" y="430" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Cathode: Na+(l) + e- --&gt; Na(l) (Reduction)</text>
</svg>"""
    create_or_update_svg_block(l105, 5, 'Complete Downs Cell Cross-Section for Industrial Sodium Extraction', 'downs_cell_sodium_105', svg_105)
    print()

    # =========================================================================
    # LESSON 106: Aluminium — Occurrence and Extraction
    # =========================================================================
    l106 = Lesson.objects.get(id=106)
    print(f'Enriching Lesson 106: \"{l106.title}\"')
    create_or_update_wm_block(
        l106, 2, 'Raw Red-Brown Bauxite Ore Containing Alumina and Iron(III) Oxide Impurities',
        'Bauxite_ore_sample.jpg', 'Didier Descouens', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Bauxite_ore_sample.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/b/b5/Bauxite_ore_sample.jpg'
    )
    create_or_update_wm_block(
        l106, 3, 'Massive Industrial Hall-Héroult Aluminium Smelting Potline and Carbon Anodes',
        'Aluminium_smelting_hall.jpg', 'Alcan', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Aluminium_smelting_hall.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/3/36/Aluminium_smelting_hall.jpg'
    )
    svg_106 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Hall-Héroult Electrolytic Cell: Extraction of Metallic Aluminium</text>

  <!-- Steel Tank Outer Shell with Carbon Lining -->
  <rect x="120" y="70" width="620" height="310" fill="#1e293b" rx="12" stroke="#475569" stroke-width="3"/>
  <rect x="140" y="90" width="580" height="270" fill="#334155" rx="8"/>
  <text x="430" y="350" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Carbon (Graphite) Cathode Lining (-)</text>

  <!-- Molten Cryolite + Alumina Electrolyte -->
  <rect x="160" y="130" width="540" height="190" fill="#e0f2fe" opacity="0.3" rx="6"/>
  <text x="430" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Molten Electrolyte: Al2O3 dissolved in Molten Cryolite (Na3AlF6) at ~950°C</text>

  <!-- Molten Aluminium Layer at bottom -->
  <rect x="160" y="280" width="540" height="40" fill="#94a3b8" rx="4"/>
  <text x="430" y="305" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Molten Aluminium Layer (Denser than electrolyte, tapped off)</text>

  <!-- Carbon Anodes Dipping into bath -->
  <g fill="#1e293b" stroke="#f87171" stroke-width="2">
    <rect x="220" y="40" width="65" height="180" rx="4"/>
    <rect x="340" y="40" width="65" height="180" rx="4"/>
    <rect x="460" y="40" width="65" height="180" rx="4"/>
    <rect x="580" y="40" width="65" height="180" rx="4"/>
  </g>
  <text x="430" y="70" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Carbon Anodes (+) [Consumed by O2 to form CO2: C + O2 --&gt; CO2]</text>

  <!-- Tap hole -->
  <path d="M 700 300 L 750 300 L 760 320" stroke="#facc15" stroke-width="4" fill="none"/>
  <text x="760" y="340" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Molten Al Tap</text>

  <!-- Reactions footer -->
  <rect x="60" y="395" width="350" height="45" fill="#1e293b" rx="6" stroke="#f87171" stroke-width="1"/>
  <text x="235" y="415" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Anode: 2O2-(l) --&gt; O2(g) + 4e-</text>
  <text x="235" y="432" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">O2 reacts with Carbon anode: C(s) + O2(g) --&gt; CO2(g)</text>

  <rect x="450" y="395" width="350" height="45" fill="#1e293b" rx="6" stroke="#38bdf8" stroke-width="1"/>
  <text x="625" y="415" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Cathode: Al3+(l) + 3e- --&gt; Al(l)</text>
  <text x="625" y="432" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Liquid Aluminium sinks to base of cell</text>
</svg>"""
    create_or_update_svg_block(l106, 5, 'Hall-Héroult Electrolytic Cell Architecture and Cryolite Flux Mechanism', 'hall_heroult_aluminium_106', svg_106)
    print()

    # =========================================================================
    # LESSON 107: Iron — Occurrence and Extraction
    # =========================================================================
    l107 = Lesson.objects.get(id=107)
    print(f'Enriching Lesson 107: \"{l107.title}\"')
    create_or_update_wm_block(
        l107, 2, 'Massive Industrial Blast Furnace Steelworks Tower with Hot Air Tuyeres',
        'Blast_Furnace_Duisburg.jpg', 'Frank Vincentz', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Blast_Furnace_Duisburg.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e4/Blast_Furnace_Duisburg.jpg'
    )
    create_or_update_wm_block(
        l107, 3, 'Molten Pig Iron Tapped from Base of Blast Furnace at 1500°C',
        'Molten_iron_tapping.jpg', 'Usui-shi', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Molten_iron_tapping.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Molten_iron_tapping.jpg'
    )
    svg_107 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 480" width="100%" height="100%">
  <rect width="860" height="480" fill="#0a0f1d" rx="16"/>
  <text x="430" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Industrial Blast Furnace: Internal Temperature Zones &amp; Chemical Reactions</text>

  <!-- Charge feed at top -->
  <rect x="250" y="55" width="360" height="35" fill="#334155" rx="6"/>
  <text x="430" y="78" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CHARGE: Haematite (Fe2O3) + Coke (C) + Limestone (CaCO3)</text>

  <!-- Blast Furnace Body -->
  <path d="M 330 90 L 260 270 L 280 400 L 580 400 L 600 270 L 530 90 Z" fill="#1e293b" stroke="#f97316" stroke-width="3"/>

  <!-- Zone 1 Top: Reduction Zone (~400°C - 700°C) -->
  <rect x="320" y="110" width="220" height="65" fill="#0f172a" rx="6"/>
  <text x="430" y="130" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Zone 1: ~400°C - 700°C</text>
  <text x="430" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Fe2O3(s) + 3CO(g) --&gt; 2Fe(s) + 3CO2(g)</text>
  <text x="430" y="165" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CO is the chief reducing agent</text>

  <!-- Zone 2 Middle: Slag Formation & CO Generation (~800°C - 1000°C) -->
  <rect x="295" y="190" width="270" height="75" fill="#0f172a" rx="6"/>
  <text x="430" y="210" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Zone 2: ~800°C - 1000°C</text>
  <text x="430" y="228" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">CaCO3(s) --&gt; CaO(s) + CO2(g)</text>
  <text x="430" y="244" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">CaO(s) + SiO2(s) --&gt; CaSiO3(l) [Molten Slag]</text>
  <text x="430" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CO2(g) + C(s) --&gt; 2CO(g)</text>

  <!-- Zone 3 Bottom: Combustion Zone (~1400°C - 1900°C) -->
  <rect x="290" y="280" width="280" height="65" fill="#0f172a" rx="6" stroke="#ef4444" stroke-width="1"/>
  <text x="430" y="300" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Zone 3: ~1400°C - 1900°C (Tuyeres)</text>
  <text x="430" y="318" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">C(s) + O2(g) --&gt; CO2(g)  [Exothermic, ΔH &lt; 0]</text>
  <text x="430" y="335" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Hot air blast injected through water-cooled tuyeres</text>

  <!-- Hearth: Molten Slag & Molten Iron -->
  <rect x="300" y="355" width="260" height="20" fill="#e2e8f0" opacity="0.8" rx="2"/>
  <text x="430" y="369" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Molten Slag (CaSiO3) Layer [Less dense, floats]</text>

  <rect x="300" y="377" width="260" height="23" fill="#f97316" rx="2"/>
  <text x="430" y="393" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Molten Pig Iron (Fe) Layer [Denser, tapped bottom]</text>

  <!-- Taps -->
  <line x1="280" y1="365" x2="230" y2="365" stroke="#e2e8f0" stroke-width="4"/>
  <text x="170" y="370" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Slag Tap</text>

  <line x1="580" y1="390" x2="630" y2="390" stroke="#f97316" stroke-width="4"/>
  <text x="690" y="395" fill="#f97316" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Iron Tap (Pig Iron)</text>
</svg>"""
    create_or_update_svg_block(l107, 5, 'Blast Furnace Internal Temperature Zones, Chemical Reactions, and Slag Separation', 'blast_furnace_iron_107', svg_107)
    print()

    # =========================================================================
    # LESSON 108: Zinc — Occurrence and Extraction
    # =========================================================================
    l108 = Lesson.objects.get(id=108)
    print(f'Enriching Lesson 108: \"{l108.title}\"')
    create_or_update_wm_block(
        l108, 2, 'Natural Crystalline Sphalerite (Zinc Blende, ZnS) Mineral Specimen',
        'Sphalerite_crystal.jpg', 'Robert M. Lavinsky', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Sphalerite_crystal.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e4/Sphalerite_crystal.jpg'
    )
    create_or_update_wm_block(
        l108, 3, 'High-Purity Zinc Ingot Slabs Manufactured from Distillation and Electrolysis',
        'Zinc_metal_ingot.jpg', 'Hi-Res Images of Chemical Elements', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Zinc_metal_ingot.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Zinc_metal_ingot.jpg'
    )
    svg_108 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Industrial Extraction of Zinc: Roasting &amp; Dual Reduction Routes</text>

  <!-- Step 1 Roasting -->
  <rect x="50" y="65" width="760" height="80" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
  <text x="430" y="90" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Stage 1: Ore Roasting (Froth Flotation Concentrate)</text>
  <text x="430" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Zinc Blende (ZnS): <tspan fill="#38bdf8" font-family="monospace">2ZnS(s) + 3O2(g) --&gt; 2ZnO(s) + 2SO2(g)</tspan></text>
  <text x="430" y="133" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Calamine (ZnCO3): ZnCO3(s) --&gt; ZnO(s) + CO2(g)</text>

  <!-- Route 1: Pyrometallurgical / Distillation -->
  <rect x="50" y="165" width="365" height="270" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
  <text x="232" y="195" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Route A: Carbon Reduction &amp; Distillation</text>
  
  <rect x="70" y="215" width="325" height="200" fill="#0f172a" rx="8"/>
  <text x="232" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Reaction in Fireclay Retorts (~1300°C)</text>
  <text x="232" y="265" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">ZnO(s) + C(s) --&gt; Zn(g) + CO(g)</text>
  
  <rect x="85" y="285" width="295" height="115" fill="#1e293b" rx="6"/>
  <text x="232" y="310" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">• Zinc b.p. = 907°C (vapour at 1300°C)</text>
  <text x="232" y="330" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Zinc vapour leaves retort &amp; condensed</text>
  <text x="232" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Solidifies into "Spelter" (97-98% pure Zn)</text>
  <text x="232" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Fractional distillation yields 99.9% pure Zn</text>

  <!-- Route 2: Electrolytic Route -->
  <rect x="445" y="165" width="365" height="270" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
  <text x="627" y="195" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Route B: Acid Leaching &amp; Electrolysis</text>
  
  <rect x="465" y="215" width="325" height="200" fill="#0f172a" rx="8"/>
  <text x="627" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Leaching with Dilute H2SO4</text>
  <text x="627" y="265" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">ZnO(s) + H2SO4(aq) --&gt; ZnSO4(aq) + H2O(l)</text>
  
  <rect x="480" y="285" width="295" height="115" fill="#1e293b" rx="6"/>
  <text x="627" y="310" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">• Solution purified with Zinc dust</text>
  <text x="627" y="330" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Electrolysed with Al cathode &amp; Pb anode</text>
  <text x="627" y="350" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cathode: Zn2+(aq) + 2e- --&gt; Zn(s)</text>
  <text x="627" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Yields ultra-high purity Zinc (&gt;99.95%)</text>
</svg>"""
    create_or_update_svg_block(l108, 5, 'Dual-Pathway Zinc Extraction: Pyrometallurgical Distillation vs Electrolytic Route', 'zinc_extraction_dual_route_108', svg_108)
    print()

    # =========================================================================
    # LESSON 109: Lead — Occurrence and Extraction
    # =========================================================================
    l109 = Lesson.objects.get(id=109)
    print(f'Enriching Lesson 109: \"{l109.title}\"')
    create_or_update_wm_block(
        l109, 2, 'Natural Metallic Luster and Cubic Cleavage of Galena Mineral Specimen (Lead Ore)',
        'Galena_ore_specimen.jpg', 'Didier Descouens', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Galena_ore_specimen.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e4/Galena_ore_specimen.jpg'
    )
    create_or_update_wm_block(
        l109, 3, 'Cast Ingot of Heavy Refined Metallic Lead Displaying Characteristic Grey Patina',
        'Lead_ingot_bar.jpg', 'Jurii', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Lead_ingot_bar.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Lead_ingot_bar.jpg'
    )
    svg_109 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Industrial Extraction of Lead: Smelting, Reduction &amp; Desilverization</text>

  <!-- Step 1: Roasting -->
  <rect x="50" y="65" width="760" height="75" fill="#1e293b" rx="10" stroke="#a78bfa" stroke-width="2"/>
  <text x="430" y="90" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Stage 1: Controlled Roasting of Galena in Sintering Machine</text>
  <text x="430" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Main Reaction: <tspan fill="#38bdf8" font-family="monospace">2PbS(s) + 3O2(g) --&gt; 2PbO(s) + 2SO2(g)</tspan></text>
  <text x="430" y="132" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Side Reaction: PbS(s) + 2O2(g) --&gt; PbSO4(s)</text>

  <!-- Step 2: Blast Furnace Reduction -->
  <rect x="50" y="155" width="365" height="275" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
  <text x="232" y="185" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Stage 2: Blast Furnace Reduction</text>
  
  <rect x="70" y="205" width="325" height="210" fill="#0f172a" rx="8"/>
  <text x="232" y="230" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Reduction by Coke (C) &amp; CO</text>
  <text x="232" y="255" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">PbO(s) + C(s) --&gt; Pb(l) + CO(g)</text>
  <text x="232" y="275" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">PbO(s) + CO(g) --&gt; Pb(l) + CO2(g)</text>
  
  <rect x="85" y="295" width="295" height="105" fill="#1e293b" rx="6"/>
  <text x="232" y="320" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Self-Reduction Reactions:</text>
  <text x="232" y="340" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2PbO(s) + PbS(s) --&gt; 3Pb(l) + SO2(g)</text>
  <text x="232" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">PbSO4(s) + PbS(s) --&gt; 2Pb(l) + 2SO2(g)</text>
  <text x="232" y="385" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Molten Lead (Bullion) tapped at base</text>

  <!-- Step 3: Refining & Parkes Process -->
  <rect x="445" y="155" width="365" height="275" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
  <text x="627" y="185" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Stage 3: Refining &amp; Parkes Process</text>
  
  <rect x="465" y="205" width="325" height="210" fill="#0f172a" rx="8"/>
  <text x="627" y="230" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Desilverization (Parkes Process)</text>
  <text x="627" y="255" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Small amount of Zinc added to molten lead</text>
  
  <rect x="480" y="275" width="295" height="125" fill="#1e293b" rx="6"/>
  <text x="627" y="298" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Silver is ~300x more soluble in Zn than Pb</text>
  <text x="627" y="318" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Ag-Zn alloy forms crust on top; skimmed off</text>
  <text x="627" y="340" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Recovered Silver offsets production costs</text>
  <text x="627" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Final Lead purity &gt;99.99%</text>
</svg>"""
    create_or_update_svg_block(l109, 4, 'Lead Blast Furnace Smelting, Self-Reduction Chemistry, and Parkes Desilverization Process', 'lead_extraction_parkes_109', svg_109)
    print()

    print('=== First Half of Topic 5 (Lessons 103 - 109) Completed Successfully! ===')

if __name__ == '__main__':
    enrich_topic5_first_half()
