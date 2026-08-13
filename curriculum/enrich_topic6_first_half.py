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
    verified_url = fetch_wikimedia_api_url(filename) or fallback_url
    
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
    if not block:
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
    
    # We look for an existing block on this page or create one
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
    if not block or block.assets.filter(source_type='external').exists():
        # create separate block for SVG if existing block has external asset
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=page_num,
            block_type='suggested_diagram',
            title=title,
            component_order=15,
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

def enrich_topic6_first_half():
    print('=== ENRICHING FORM 4 TOPIC 6: ORGANIC CHEMISTRY II (FIRST HALF: LESSONS 117 - 128) ===\n')

    # =========================================================================
    # LESSON 117: Alkanols (Alcohols) — Introduction
    # =========================================================================
    l117 = Lesson.objects.get(id=117)
    print(f'Enriching Lesson 117: \"{l117.title}\"')
    create_or_update_wm_block(
        l117, 2, 'Laboratory Reagent Bottle of Pure Anhydrous Ethanol Liquid',
        'Ethanol_bottle.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Ethanol_bottle.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l117, 3, 'Traditional Oak Fermentation Casks for Yeast Alcohol Production',
        'Oak_wine_barrels.jpg', 'CEphoto, Uwe Aranas', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Oak_wine_barrels.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_117 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">From Water to Alkanols: The Hydroxyl Functional Group Structure</text>

  <!-- Left: Water vs Alkanol -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Structural Derivation from Water</text>

  <g transform="translate(65, 115)">
    <!-- Water Model -->
    <rect x="0" y="0" width="150" height="110" fill="#0f172a" rx="8"/>
    <text x="75" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Water (H2O)</text>
    <text x="75" y="65" fill="#f8fafc" font-family="monospace" font-size="18" text-anchor="middle">H — O — H</text>
    <text x="75" y="95" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Inorganic solvent</text>

    <!-- Alkanol Model -->
    <rect x="170" y="0" width="150" height="110" fill="#0f172a" rx="8" stroke="#4ade80" stroke-width="1"/>
    <text x="245" y="25" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Alkanol (R-OH)</text>
    <text x="245" y="65" fill="#facc15" font-family="monospace" font-size="18" text-anchor="middle">R — O — H</text>
    <text x="245" y="95" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Alkyl group + Hydroxyl</text>
  </g>

  <rect x="60" y="245" width="330" height="155" fill="#0f172a" rx="6"/>
  <text x="225" y="270" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">The -OH (Hydroxyl) Functional Group</text>
  <text x="225" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Replaces one Hydrogen atom of an Alkane (CnH2n+2)</text>
  <text x="225" y="320" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">General Formula: CnH2n+1OH</text>
  <text x="225" y="345" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Polar O-H bond enables hydrogen bonding</text>
  <text x="225" y="370" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Neutral character (does NOT liberate OH- ions in water)</text>

  <!-- Right: First 4 Alkanols -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. First Four Members of Homologous Series</text>

  <rect x="475" y="115" width="320" height="65" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Methanol (n = 1)</text>
  <text x="490" y="160" fill="#cbd5e1" font-family="monospace" font-size="12">CH3OH  |  Molar Mass: 32 g/mol</text>

  <rect x="475" y="190" width="320" height="65" fill="#0f172a" rx="6" stroke="#60a5fa" stroke-width="1"/>
  <text x="490" y="213" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Ethanol (n = 2)</text>
  <text x="490" y="235" fill="#cbd5e1" font-family="monospace" font-size="12">CH3CH2OH (C2H5OH)  |  Molar Mass: 46 g/mol</text>

  <rect x="475" y="265" width="320" height="65" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
  <text x="490" y="288" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Propan-1-ol (n = 3)</text>
  <text x="490" y="310" fill="#cbd5e1" font-family="monospace" font-size="12">CH3CH2CH2OH (C3H7OH)  |  Molar Mass: 60 g/mol</text>

  <rect x="475" y="340" width="320" height="65" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
  <text x="490" y="363" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Butan-1-ol (n = 4)</text>
  <text x="490" y="385" fill="#cbd5e1" font-family="monospace" font-size="12">CH3(CH2)3OH (C4H9OH)  |  Molar Mass: 74 g/mol</text>
</svg>"""
    create_or_update_svg_block(l117, 2, 'Alkanols Homologous Series and Hydroxyl Functional Group Architecture', 'alkanols_intro_117', svg_117)
    print()

    # =========================================================================
    # LESSON 118: Nomenclature and Isomerism of Alkanols
    # =========================================================================
    l118 = Lesson.objects.get(id=118)
    print(f'Enriching Lesson 118: \"{l118.title}\"')
    create_or_update_wm_block(
        l118, 2, 'Reagent Bottles of Isomeric Propan-1-ol and Propan-2-ol Liquids',
        'Propanol_isomers.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Propanol_isomers.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l118, 3, 'Laboratory Grade Butan-1-ol Bottle Showing IUPAC Nomenclature and Hazard Label',
        'Butanol_bottle.jpg', 'Benjah-bmm27', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Butanol_bottle.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_118 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Classification &amp; Isomerism of Alkanols: Primary, Secondary, and Tertiary</text>

  <!-- 3 Classes of Alcohols -->
  <g transform="translate(40, 65)">
    <!-- Primary 1° -->
    <rect x="0" y="0" width="245" height="230" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Primary (1°) Alkanol</text>
    <rect x="15" y="45" width="215" height="85" fill="#0f172a" rx="6"/>
    <text x="122" y="75" fill="#facc15" font-family="monospace" font-size="14" text-anchor="middle">R — CH2 — OH</text>
    <text x="122" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">-OH on carbon attached to 1 alkyl</text>
    <rect x="15" y="140" width="215" height="75" fill="#0f172a" rx="6"/>
    <text x="122" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Propan-1-ol</text>
    <text x="122" y="185" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">CH3-CH2-CH2-OH</text>
    <text x="122" y="203" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Oxidises to Aldehyde &amp; Acid</text>

    <!-- Secondary 2° -->
    <rect x="270" y="0" width="245" height="230" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="392" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Secondary (2°) Alkanol</text>
    <rect x="285" y="45" width="215" height="85" fill="#0f172a" rx="6"/>
    <text x="392" y="75" fill="#facc15" font-family="monospace" font-size="14" text-anchor="middle">R — CH(OH) — R'</text>
    <text x="392" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">-OH on carbon attached to 2 alkyls</text>
    <rect x="285" y="140" width="215" height="75" fill="#0f172a" rx="6"/>
    <text x="392" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Propan-2-ol</text>
    <text x="392" y="185" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">CH3-CH(OH)-CH3</text>
    <text x="392" y="203" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Oxidises to Ketone (Alkanone)</text>

    <!-- Tertiary 3° -->
    <rect x="540" y="0" width="245" height="230" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
    <text x="662" y="28" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Tertiary (3°) Alkanol</text>
    <rect x="555" y="45" width="215" height="85" fill="#0f172a" rx="6"/>
    <text x="662" y="75" fill="#facc15" font-family="monospace" font-size="14" text-anchor="middle">R3 — C — OH</text>
    <text x="662" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">-OH on carbon attached to 3 alkyls</text>
    <rect x="555" y="140" width="215" height="75" fill="#0f172a" rx="6"/>
    <text x="662" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">2-Methylpropan-2-ol</text>
    <text x="662" y="185" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">(CH3)3C-OH</text>
    <text x="662" y="203" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Resistant to Mild Oxidation</text>
  </g>

  <!-- Bottom: IUPAC Naming Rules -->
  <rect x="40" y="310" width="780" height="125" fill="#1e293b" rx="10" stroke="#64748b" stroke-width="1"/>
  <text x="430" y="335" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Four Step IUPAC Nomenclature Roadmap for Alkanols</text>
  <text x="430" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1. Identify the longest carbon chain containing the -OH group (e.g. butane --&gt; butanol)</text>
  <text x="430" y="385" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">2. Number carbon atoms from the end closest to the -OH group to give -OH lowest possible locant</text>
  <text x="430" y="410" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">3. Prefix substituent alkyl groups in alphabetical order (e.g., 2-methylbutan-1-ol)</text>
</svg>"""
    create_or_update_svg_block(l118, 2, 'Primary, Secondary, and Tertiary Alkanol Classification and IUPAC Naming Rules', 'alkanol_isomerism_118', svg_118)
    print()

    # =========================================================================
    # LESSON 119: Preparation of Alkanols
    # =========================================================================
    l119 = Lesson.objects.get(id=119)
    print(f'Enriching Lesson 119: \"{l119.title}\"')
    create_or_update_wm_block(
        l119, 2, 'Laboratory Fermentation Flask Setup with Glucose, Yeast, and Limewater Trap',
        'Laboratory_fermentation_setup.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Laboratory_fermentation_setup.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l119, 4, 'Industrial Petrochemical High-Pressure Catalytic Hydration Plant for Ethene',
        'Petrochemical_refinery_hydration.jpg', 'Seav', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Petrochemical_refinery_hydration.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_119 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Two Primary Industrial Pathways for the Preparation of Ethanol</text>

  <!-- Left: Fermentation -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#facc15" stroke-width="2"/>
  <text x="225" y="95" fill="#facc15" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Method A: Biological Fermentation</text>

  <rect x="60" y="115" width="330" height="140" fill="#0f172a" rx="8"/>
  <text x="225" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Zymase Enzyme Catalysis (~37°C, Anaerobic)</text>
  <text x="225" y="165" fill="#f8fafc" font-family="monospace" font-size="12" text-anchor="middle">C6H12O6(aq) --&gt; 2C2H5OH(aq) + 2CO2(g)</text>
  <text x="225" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Yeast enzymes denature above 40°C</text>
  <text x="225" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Air excluded to prevent oxidation to vinegar</text>
  <text x="225" y="235" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Maximum ethanol concentration ~15%</text>

  <rect x="60" y="270" width="330" height="135" fill="#0f172a" rx="6"/>
  <text x="225" y="295" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Fractional Distillation Required</text>
  <text x="225" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Ethanol (b.p. 78.4°C) distils off first</text>
  <text x="225" y="340" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Water (b.p. 100°C) condenses in fractionating column</text>
  <text x="225" y="365" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Yields 95.6% azeotropic rectified spirit</text>

  <!-- Right: Catalytic Hydration -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="635" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Method B: Catalytic Hydration of Ethene</text>

  <rect x="475" y="115" width="320" height="140" fill="#0f172a" rx="8"/>
  <text x="635" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Electrophilic Addition of Steam</text>
  <text x="635" y="165" fill="#f8fafc" font-family="monospace" font-size="12" text-anchor="middle">C2H4(g) + H2O(g) &lt;==&gt; C2H5OH(g)</text>
  <text x="635" y="195" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Operating Conditions:</text>
  <text x="635" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Catalyst: Phosphoric acid (H3PO4) on silica</text>
  <text x="635" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Temperature: 300°C | Pressure: 60 - 70 atm</text>

  <rect x="475" y="270" width="320" height="135" fill="#0f172a" rx="6"/>
  <text x="635" y="295" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Industrial Advantages</text>
  <text x="635" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Continuous high-speed process</text>
  <text x="635" y="340" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Produces 100% pure industrial ethanol directly</text>
  <text x="635" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Reversible reaction; unreacted gases recycled</text>
</svg>"""
    create_or_update_svg_block(l119, 3, 'Comparative Preparation Pathways: Yeast Fermentation vs Industrial Catalytic Hydration of Ethene', 'ethanol_prep_pathways_119', svg_119)
    print()

    # =========================================================================
    # LESSON 120: Physical Properties of Alkanols
    # =========================================================================
    l120 = Lesson.objects.get(id=120)
    print(f'Enriching Lesson 120: \"{l120.title}\"')
    create_or_update_wm_block(
        l120, 2, 'Miscibility Demonstration: Ethanol Completely Dissolving in Water Forming a Clear Homogeneous Solution',
        'Ethanol_water_miscibility.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Ethanol_water_miscibility.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l120, 4, 'Laboratory Fractional Distillation Apparatus Determining Pure Alcohol Boiling Points',
        'Fractional_distillation_lab.jpg', 'Theresa knott', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Fractional_distillation_lab.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_120 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Physical Properties: Intermolecular Hydrogen Bonding &amp; Boiling Point Trends</text>

  <!-- Left: Hydrogen Bonding -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Intermolecular Hydrogen Bonding Network</text>

  <g transform="translate(65, 120)">
    <!-- Molecule 1 -->
    <rect x="0" y="10" width="140" height="60" fill="#0f172a" rx="6"/>
    <text x="70" y="45" fill="#facc15" font-family="monospace" font-size="14" text-anchor="middle">C2H5 — O(δ-) — H(δ+)</text>

    <!-- H-Bond -->
    <line x1="140" y1="40" x2="190" y2="40" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>
    <text x="165" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">H-BOND</text>

    <!-- Molecule 2 -->
    <rect x="190" y="10" width="140" height="60" fill="#0f172a" rx="6"/>
    <text x="260" y="45" fill="#facc15" font-family="monospace" font-size="14" text-anchor="middle">O(δ-) — H(δ+) — C2H5</text>
  </g>

  <rect x="60" y="215" width="330" height="185" fill="#0f172a" rx="6"/>
  <text x="225" y="240" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Effects of Hydrogen Bonding</text>
  <text x="225" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Much higher boiling points than alkanes of similar mass</text>
  <text x="225" y="288" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Ethanol (Mr = 46): b.p. 78.4°C vs Propane (Mr = 44): -42°C</text>
  <text x="225" y="310" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Complete miscibility with water for lower members (C1-C3)</text>
  <text x="225" y="333" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Higher members become progressively insoluble in water</text>
  <text x="225" y="358" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">(Non-polar hydrocarbon chain dominates over polar -OH)</text>

  <!-- Right: Trends -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Homologous Series Property Trends</text>

  <rect x="475" y="115" width="320" height="65" fill="#0f172a" rx="6"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Boiling Point Elevation</text>
  <text x="490" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Increases regularly with molecular mass (stronger van der Waals forces)</text>

  <rect x="475" y="190" width="320" height="65" fill="#0f172a" rx="6"/>
  <text x="490" y="213" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Viscosity &amp; Density Increase</text>
  <text x="490" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Higher members are oily liquids, while C12+ are waxy solids</text>

  <rect x="475" y="265" width="320" height="65" fill="#0f172a" rx="6"/>
  <text x="490" y="288" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Volatility &amp; Solubility Decrease</text>
  <text x="490" y="310" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Evaporation rate falls as intermolecular cohesion increases</text>

  <rect x="475" y="340" width="320" height="65" fill="#0f172a" rx="6"/>
  <text x="490" y="363" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Non-Electrolyte Electrical Neutrality</text>
  <text x="490" y="385" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Do not conduct electric current in pure state or aqueous solution</text>
</svg>"""
    create_or_update_svg_block(l120, 3, 'Intermolecular Hydrogen Bonding Network and Homologous Physical Property Trends', 'alkanol_hbonding_trends_120', svg_120)
    print()

    # =========================================================================
    # LESSON 121: Chemical Properties of Alkanols
    # =========================================================================
    l121 = Lesson.objects.get(id=121)
    print(f'Enriching Lesson 121: \"{l121.title}\"')
    create_or_update_wm_block(
        l121, 4, 'Effervescence of Hydrogen Gas as Sodium Metal Reacts Exothermically with Pure Ethanol',
        'Sodium_reacting_with_ethanol.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Sodium_reacting_with_ethanol.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l121, 6, 'Color Transition of Acidified Potassium Dichromate(VI) from Orange to Green During Ethanol Oxidation',
        'Potassium_dichromate_oxidation.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Potassium_dichromate_oxidation.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_121 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Four Core Chemical Reaction Pathways of Alkanols</text>

  <g transform="translate(40, 65)">
    <!-- 1. Combustion -->
    <rect x="0" y="0" width="370" height="160" fill="#1e293b" rx="10" stroke="#f97316" stroke-width="2"/>
    <text x="185" y="28" fill="#f97316" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Complete Combustion (Exothermic Fuel)</text>
    <rect x="15" y="45" width="340" height="100" fill="#0f172a" rx="6"/>
    <text x="185" y="70" fill="#f8fafc" font-family="monospace" font-size="12" text-anchor="middle">C2H5OH(l) + 3O2(g) --&gt; 2CO2(g) + 3H2O(l)</text>
    <text x="185" y="95" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">ΔH = -1368 kJ/mol (Clean blue non-smoky flame)</text>
    <text x="185" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Used as renewable biofuel (Gasohol)</text>

    <!-- 2. Reaction with Sodium Metal -->
    <rect x="410" y="0" width="370" height="160" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="595" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Reaction with Sodium Metal</text>
    <rect x="425" y="45" width="340" height="100" fill="#0f172a" rx="6"/>
    <text x="595" y="70" fill="#f8fafc" font-family="monospace" font-size="12" text-anchor="middle">2C2H5OH(l) + 2Na(s) --&gt; 2C2H5ONa(eth) + H2(g)</text>
    <text x="595" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Forms Sodium Ethoxide + Hydrogen gas (Effervescence)</text>
    <text x="595" y="125" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Milder than reaction of sodium with water</text>

    <!-- 3. Controlled Oxidation -->
    <rect x="0" y="180" width="370" height="180" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="185" y="208" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. Controlled Oxidation (H+/Cr2O7 2-)</text>
    <rect x="15" y="225" width="340" height="120" fill="#0f172a" rx="6"/>
    <text x="185" y="250" fill="#fbbf24" font-family="monospace" font-size="11" text-anchor="middle">Step 1: C2H5OH + [O] --&gt; CH3CHO + H2O (Ethanal)</text>
    <text x="185" y="275" fill="#4ade80" font-family="monospace" font-size="11" text-anchor="middle">Step 2: CH3CHO + [O] --&gt; CH3COOH (Ethanoic Acid)</text>
    <text x="185" y="305" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Orange Cr2O7(2-) reduced to Green Cr3+ ions</text>
    <text x="185" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Foundation of Breathalyzer alcohol test</text>

    <!-- 4. Acid Dehydration -->
    <rect x="410" y="180" width="370" height="180" fill="#1e293b" rx="10" stroke="#a78bfa" stroke-width="2"/>
    <text x="595" y="208" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4. Dehydration to Alkenes (Conc. H2SO4)</text>
    <rect x="425" y="225" width="340" height="120" fill="#0f172a" rx="6"/>
    <text x="595" y="250" fill="#f8fafc" font-family="monospace" font-size="12" text-anchor="middle">C2H5OH(l) --[Conc H2SO4 / 170°C]--&gt; C2H4(g) + H2O</text>
    <text x="595" y="280" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Elimination of water molecule produces Ethene</text>
    <text x="595" y="305" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">At 140°C in excess ethanol: produces Diethyl Ether</text>
    <text x="595" y="328" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Catalyst: Al2O3 at 350°C also effective</text>
  </g>
</svg>"""
    create_or_update_svg_block(l121, 2, 'Chemical Reaction Pathways of Alkanols: Combustion, Sodium Metal, Oxidation, and Dehydration', 'alkanol_chemical_reactions_121', svg_121)
    print()

    # =========================================================================
    # LESSON 122: Uses and Health Effects of Alkanols
    # =========================================================================
    l122 = Lesson.objects.get(id=122)
    print(f'Enriching Lesson 122: \"{l122.title}\"')
    create_or_update_wm_block(
        l122, 2, 'Bio-Ethanol Fuel Pump Dispenser for Motor Vehicles',
        'E85_bioethanol_fuel_pump.jpg', 'Mattes', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:E85_bioethanol_fuel_pump.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l122, 3, 'Ethanol-Based Antiseptic Hand Sanitizer Gel and Disinfectant Bottles',
        'Hand_sanitizer_bottles.jpg', 'Prathyush Thomas', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Hand_sanitizer_bottles.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_122 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Comparative Biochemistry &amp; Toxicity: Ethanol vs. Lethal Methanol</text>

  <!-- Left: Ethanol Metabolism -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Ethanol Metabolism in the Liver</text>

  <rect x="60" y="115" width="330" height="140" fill="#0f172a" rx="8"/>
  <text x="225" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Alcohol Dehydrogenase Pathway</text>
  <text x="225" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">CH3CH2OH --[ADH]--&gt; CH3CHO (Ethanal)</text>
  <text x="225" y="190" fill="#4ade80" font-family="monospace" font-size="11" text-anchor="middle">CH3CHO --[ALDH]--&gt; CH3COOH (Ethanoic Acid)</text>
  <text x="225" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Ethanoic acid broken down to CO2 + H2O</text>
  <text x="225" y="235" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Excess consumption leads to cirrhosis &amp; addiction</text>

  <rect x="60" y="270" width="330" height="135" fill="#0f172a" rx="6"/>
  <text x="225" y="295" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Major Industrial Applications</text>
  <text x="225" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Universal organic solvent for perfumes, paints, varnishes</text>
  <text x="225" y="342" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Pharmaceutical preservative &amp; antiseptic sanitizer</text>
  <text x="225" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Renewable biofuel blended in petrol (E10, E85)</text>

  <!-- Right: Methanol Poisoning -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="635" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. The Lethal Danger of Methanol (CH3OH)</text>

  <rect x="475" y="115" width="320" height="140" fill="#0f172a" rx="8" stroke="#ef4444" stroke-width="1"/>
  <text x="635" y="140" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Toxic Oxidation to Methanoic Acid</text>
  <text x="635" y="165" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">CH3OH --[ADH]--&gt; HCHO (Formaldehyde)</text>
  <text x="635" y="190" fill="#ef4444" font-family="monospace" font-size="11" text-anchor="middle">HCHO --[ALDH]--&gt; HCOOH (Formic Acid)</text>
  <text x="635" y="215" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">HCOOH destroys optic nerve --&gt; Permanent Blindness</text>
  <text x="635" y="235" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Causes severe metabolic acidosis and death</text>

  <rect x="475" y="270" width="320" height="135" fill="#0f172a" rx="6"/>
  <text x="635" y="295" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Methylated Spirits Safety Notice</text>
  <text x="635" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Industrial ethanol denatured with ~10% methanol</text>
  <text x="635" y="342" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Pyridine added for foul odor + purple dye</text>
  <text x="635" y="365" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Strictly unfit for human consumption</text>
</svg>"""
    create_or_update_svg_block(l122, 4, 'Comparative Metabolic Pathways and Toxicity: Ethanol vs Toxic Methanol', 'alkanol_toxicity_uses_122', svg_122)
    print()

    # =========================================================================
    # LESSON 123: Alkanoic Acids (Carboxylic Acids) — Introduction
    # =========================================================================
    l123 = Lesson.objects.get(id=123)
    print(f'Enriching Lesson 123: \"{l123.title}\"')
    create_or_update_wm_block(
        l123, 2, 'Natural Citrus Fruits Containing Citric Acid and Fermented Vinegar (Dilute Ethanoic Acid)',
        'Vinegar_and_citrus_fruits.jpg', 'Evan-Amos', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Vinegar_and_citrus_fruits.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l123, 3, 'Stinging Nettle Leaf (Urtica dioica) Secreting Natural Methanoic Acid (Formic Acid)',
        'Stinging_nettle_leaf.jpg', 'Didier Descouens', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Stinging_nettle_leaf.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_123 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Carboxyl Functional Group (-COOH): Electronic Structure &amp; Homologous Series</text>

  <!-- Left: Carboxyl Group Anatomy -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. The Carboxyl Group (-COOH) Anatomy</text>

  <g transform="translate(65, 115)">
    <rect x="0" y="0" width="320" height="120" fill="#0f172a" rx="8"/>
    <!-- C=O and C-OH -->
    <text x="160" y="45" fill="#facc15" font-family="monospace" font-size="18" text-anchor="middle">O</text>
    <text x="160" y="60" fill="#facc15" font-family="monospace" font-size="18" text-anchor="middle">║</text>
    <text x="160" y="80" fill="#f8fafc" font-family="monospace" font-size="16" text-anchor="middle">R — C — O — H</text>
    <text x="60" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Carbonyl Group</text>
    <text x="260" y="105" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Hydroxyl Group</text>
  </g>

  <rect x="60" y="255" width="330" height="145" fill="#0f172a" rx="6"/>
  <text x="225" y="280" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Hybrid Electronic Properties</text>
  <text x="225" y="305" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Highly electronegative C=O oxygen withdraws electron density</text>
  <text x="225" y="328" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Weakens O-H bond, allowing H+ to ionize in water (Acidic)</text>
  <text x="225" y="352" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">General Formula: CnH2n+1COOH (or CnH2nO2)</text>
  <text x="225" y="375" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Where n = 0, 1, 2, 3... (n=0 for methanoic acid)</text>

  <!-- Right: First 4 Members -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. First Four Members &amp; Natural Sources</text>

  <rect x="475" y="115" width="320" height="65" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Methanoic Acid (HCOOH)</text>
  <text x="490" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Formic acid. Natural source: Ant stings &amp; stinging nettles.</text>

  <rect x="475" y="190" width="320" height="65" fill="#0f172a" rx="6" stroke="#60a5fa" stroke-width="1"/>
  <text x="490" y="213" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Ethanoic Acid (CH3COOH)</text>
  <text x="490" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Acetic acid. Natural source: Fermented wine / vinegar.</text>

  <rect x="475" y="265" width="320" height="65" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
  <text x="490" y="288" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Propanoic Acid (CH3CH2COOH)</text>
  <text x="490" y="310" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Propionic acid. Natural source: Fermented Swiss cheese.</text>

  <rect x="475" y="340" width="320" height="65" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
  <text x="490" y="363" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Butanoic Acid (CH3(CH2)2COOH)</text>
  <text x="490" y="385" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Butyric acid. Natural source: Rancid butter &amp; sweat.</text>
</svg>"""
    create_or_update_svg_block(l123, 5, 'Carboxyl Group Electronic Polarization and First Four Homologous Members', 'alkanoic_intro_123', svg_123)
    print()

    # =========================================================================
    # LESSON 124: Nomenclature of Alkanoic Acids
    # =========================================================================
    l124 = Lesson.objects.get(id=124)
    print(f'Enriching Lesson 124: \"{l124.title}\"')
    create_or_update_wm_block(
        l124, 2, 'Laboratory Reagent Bottle of Pure Methanoic Acid Showing IUPAC Label',
        'Formic_acid_bottle.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Formic_acid_bottle.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l124, 3, 'Sample of Butanoic Acid Liquid Exhibiting Characteristic Pungent Chemical Odor',
        'Butyric_acid_sample.jpg', 'Benjah-bmm27', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Butyric_acid_sample.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_124 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Systematic IUPAC Nomenclature of Straight &amp; Branched Alkanoic Acids</text>

  <!-- Left: Straight Chain Naming -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Straight-Chain IUPAC Naming Rules</text>

  <rect x="60" y="115" width="330" height="135" fill="#0f172a" rx="8"/>
  <text x="225" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Rule: Replace "-e" of alkane with "-oic acid"</text>
  <text x="225" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Methane (CH4) --&gt; Methanoic Acid (HCOOH)</text>
  <text x="225" y="188" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Ethane (C2H6) --&gt; Ethanoic Acid (CH3COOH)</text>
  <text x="225" y="212" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Propane (C3H8) --&gt; Propanoic Acid (C2H5COOH)</text>
  <text x="225" y="235" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Butane (C4H10) --&gt; Butanoic Acid (C3H7COOH)</text>

  <rect x="60" y="265" width="330" height="140" fill="#0f172a" rx="6"/>
  <text x="225" y="290" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Key Numbering Rule</text>
  <text x="225" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• The Carboxyl carbon (-COOH) is ALWAYS Carbon-1 (C1)</text>
  <text x="225" y="338" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• No locant number needed for -COOH group itself</text>
  <text x="225" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Always occupies terminal position on the main chain</text>
  <text x="225" y="385" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Contains 1 double bond (C=O) and 1 single bond (C-OH)</text>

  <!-- Right: Branched Chains -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Branched-Chain Examples &amp; Isomerism</text>

  <rect x="475" y="115" width="320" height="90" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">2-Methylpropanoic Acid (C4H8O2)</text>
  <text x="490" y="160" fill="#cbd5e1" font-family="monospace" font-size="12">CH3 — CH(CH3) — COOH</text>
  <text x="490" y="180" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Chain isomer of butanoic acid (Isobutyric acid)</text>

  <rect x="475" y="220" width="320" height="90" fill="#0f172a" rx="8" stroke="#fbbf24" stroke-width="1"/>
  <text x="490" y="243" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">2-Chloropropanoic Acid</text>
  <text x="490" y="265" fill="#cbd5e1" font-family="monospace" font-size="12">CH3 — CH(Cl) — COOH</text>
  <text x="490" y="285" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Halogen-substituted alkanoic acid (Stronger acid)</text>

  <rect x="475" y="325" width="320" height="80" fill="#0f172a" rx="6"/>
  <text x="635" y="350" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Summary of Functional Isomerism</text>
  <text x="635" y="375" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Alkanoic acids are functional group isomers of Esters</text>
  <text x="635" y="395" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Both share the general molecular formula CnH2nO2</text>
</svg>"""
    create_or_update_svg_block(l124, 4, 'Systematic IUPAC Nomenclature and Isomerism Roadmap for Carboxylic Acids', 'alkanoic_nomenclature_124', svg_124)
    print()

    # =========================================================================
    # LESSON 125: Laboratory Preparation of Ethanoic Acid
    # =========================================================================
    l125 = Lesson.objects.get(id=125)
    print(f'Enriching Lesson 125: \"{l125.title}\"')
    create_or_update_wm_block(
        l125, 2, 'Laboratory Allihn Reflux Condenser Apparatus Setup for Organic Synthesis',
        'Laboratory_reflux_apparatus.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Laboratory_reflux_apparatus.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l125, 6, 'Laboratory Distillation Setup for Separating Pure Ethanoic Acid from Reaction Mixture',
        'Distillation_setup_lab.jpg', 'Theresa knott', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Distillation_setup_lab.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_125 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Laboratory Preparation of Ethanoic Acid: Reflux Oxidation &amp; Distillation</text>

  <!-- Left: Reflux Setup -->
  <rect x="40" y="65" width="370" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Reflux Setup (Complete Oxidation)</text>

  <rect x="70" y="115" width="310" height="180" fill="#0f172a" rx="8"/>
  <!-- Flask & Condenser -->
  <circle cx="225" cy="240" r="45" fill="#1e293b" stroke="#f97316" stroke-width="2"/>
  <text x="225" y="245" fill="#facc15" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Ethanol + H+/Cr2O7 2-</text>
  <rect x="215" y="125" width="20" height="85" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="2"/>
  <text x="295" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10">Vertical Liebig Condenser</text>
  <text x="295" y="180" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">(Vapours condense &amp; fall back)</text>

  <rect x="60" y="305" width="330" height="110" fill="#0f172a" rx="6"/>
  <text x="225" y="328" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Why Reflux is Critical</text>
  <text x="225" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Prevents escape of volatile intermediate ethanal (b.p. 21°C)</text>
  <text x="225" y="372" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Ensures 100% conversion of ethanol to ethanoic acid</text>
  <text x="225" y="395" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Orange Cr2O7(2-) turns deep green (Cr3+)</text>

  <!-- Right: Two-Step Oxidation Equations -->
  <rect x="450" y="65" width="370" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Two-Step Oxidation &amp; Distillation</text>

  <rect x="475" y="115" width="320" height="110" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Step 1: Oxidation to Ethanal</text>
  <text x="490" y="160" fill="#f8fafc" font-family="monospace" font-size="11">C2H5OH + [O] --&gt; CH3CHO + H2O</text>
  <text x="490" y="180" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Alcohol dehydrogenase / Acidified dichromate</text>
  <text x="490" y="200" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10">If distilled immediately, ethanal is collected</text>

  <rect x="475" y="235" width="320" height="110" fill="#0f172a" rx="8" stroke="#4ade80" stroke-width="1"/>
  <text x="490" y="258" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Step 2: Oxidation to Ethanoic Acid</text>
  <text x="490" y="280" fill="#f8fafc" font-family="monospace" font-size="11">CH3CHO + [O] --&gt; CH3COOH</text>
  <text x="490" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Further oxidation by excess oxidizing agent under reflux</text>
  <text x="490" y="325" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Overall: C2H5OH + 2[O] --&gt; CH3COOH + H2O</text>

  <rect x="475" y="355" width="320" height="60" fill="#0f172a" rx="6"/>
  <text x="635" y="378" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Purification: Distil reaction mixture at 118°C</text>
  <text x="635" y="398" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Pure ethanoic acid distils over as clear pungent liquid</text>
</svg>"""
    create_or_update_svg_block(l125, 4, 'Laboratory Reflux Apparatus Setup and Two-Step Oxidation Pathway for Ethanoic Acid', 'ethanoic_acid_prep_125', svg_125)
    print()

    # =========================================================================
    # LESSON 126: Physical Properties of Alkanoic Acids
    # =========================================================================
    l126 = Lesson.objects.get(id=126)
    print(f'Enriching Lesson 126: \"{l126.title}\"')
    create_or_update_wm_block(
        l126, 2, 'Solid Glacial Ethanoic Acid Crystals Formed Upon Freezing Below 16.6°C',
        'Glacial_acetic_acid_ice.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Glacial_acetic_acid_ice.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l126, 5, 'Universal Indicator Paper Showing Orange-Red Acidic pH in Aqueous Ethanoic Acid',
        'Universal_indicator_ethanoic_acid.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Universal_indicator_ethanoic_acid.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_126 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Carboxylic Acid Physical Properties: Stable Dimerization &amp; Boiling Points</text>

  <!-- Left: Dimer Formation -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Cyclic Dimer Formation via Dual H-Bonds</text>

  <g transform="translate(65, 115)">
    <rect x="0" y="0" width="320" height="130" fill="#0f172a" rx="8"/>
    <!-- Dimer structure -->
    <text x="60" y="45" fill="#facc15" font-family="monospace" font-size="13">R — C</text>
    <text x="120" y="35" fill="#f87171" font-family="monospace" font-size="13">= O • • • H — O</text>
    <text x="260" y="45" fill="#facc15" font-family="monospace" font-size="13">C — R</text>
    
    <text x="120" y="95" fill="#4ade80" font-family="monospace" font-size="13">O — H • • • O =</text>
    
    <text x="160" y="118" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Two Intermolecular Hydrogen Bonds per Dimer</text>
  </g>

  <rect x="60" y="260" width="330" height="145" fill="#0f172a" rx="6"/>
  <text x="225" y="285" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Why Carboxylic Acids Boil Higher than Alkanols</text>
  <text x="225" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Dimerization effectively doubles apparent molar mass</text>
  <text x="225" y="330" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Ethanoic Acid (Mr = 60): b.p. 118°C vs Propan-1-ol (Mr = 60): 97°C</text>
  <text x="225" y="352" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• High thermal energy required to break dual hydrogen bond ring</text>
  <text x="225" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Dimers persist even in vapour phase near boiling point</text>

  <!-- Right: Solubility & Acidity -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Solubility &amp; Weak Acid Ionization</text>

  <rect x="475" y="115" width="320" height="85" fill="#0f172a" rx="6"/>
  <text x="490" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Complete Aqueous Miscibility (C1 - C4)</text>
  <text x="490" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Form strong hydrogen bonds with water molecules</text>
  <text x="490" y="180" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Solubility drops rapidly for pentanoic acid and above</text>

  <rect x="475" y="210" width="320" height="110" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
  <text x="490" y="233" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Partial Ionization (Weak Acid)</text>
  <text x="490" y="255" fill="#f8fafc" font-family="monospace" font-size="11">CH3COOH(aq) &lt;==&gt; CH3COO-(aq) + H+(aq)</text>
  <text x="490" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Only ~1% of molecules ionize in 0.1 M solution (pH ~3)</text>
  <text x="490" y="298" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10">Turns blue litmus paper red (Weak electrolyte)</text>

  <rect x="475" y="330" width="320" height="75" fill="#0f172a" rx="6"/>
  <text x="635" y="355" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Glacial Ethanoic Acid Definition</text>
  <text x="635" y="375" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Pure anhydrous ethanoic acid (m.p. 16.6°C) freezes into</text>
  <text x="635" y="393" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">ice-like crystals on cold days in the laboratory</text>
</svg>"""
    create_or_update_svg_block(l126, 3, 'Carboxylic Acid Cyclic Dimerization Mechanism, Boiling Point Elevation, and Weak Acid Ionization', 'alkanoic_dimer_properties_126', svg_126)
    print()

    # =========================================================================
    # LESSON 127: Chemical Properties of Alkanoic Acids
    # =========================================================================
    l127 = Lesson.objects.get(id=127)
    print(f'Enriching Lesson 127: \"{l127.title}\"')
    create_or_update_wm_block(
        l127, 3, 'Rapid Effervescence of Carbon Dioxide Gas Upon Adding Sodium Carbonate to Ethanoic Acid',
        'Carbonate_acid_effervescence.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Carbonate_acid_effervescence.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l127, 6, 'Sweet Fruity Ester Layer Formed During Fischer Esterification Reaction in Warm Water Bath',
        'Esterification_water_bath.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Esterification_water_bath.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_127 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Chemical Reactions of Alkanoic Acids: Acidic Behaviour &amp; Esterification</text>

  <g transform="translate(40, 65)">
    <!-- 1. Reaction with Reactive Metals -->
    <rect x="0" y="0" width="370" height="160" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="185" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Reaction with Reactive Metals (Mg, Zn, Na)</text>
    <rect x="15" y="45" width="340" height="100" fill="#0f172a" rx="6"/>
    <text x="185" y="70" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">2CH3COOH + Mg --&gt; (CH3COO)2Mg + H2(g)</text>
    <text x="185" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Produces Magnesium Ethanoate salt + Hydrogen gas</text>
    <text x="185" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Effervescence; gas pops with burning splint</text>

    <!-- 2. Carbonates & Hydrogencarbonates -->
    <rect x="410" y="0" width="370" height="160" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="595" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Carbonates &amp; Hydrogencarbonates</text>
    <rect x="425" y="45" width="340" height="100" fill="#0f172a" rx="6"/>
    <text x="595" y="70" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">2CH3COOH + Na2CO3 --&gt; 2CH3COONa + H2O + CO2(g)</text>
    <text x="595" y="95" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">CH3COOH + NaHCO3 --&gt; CH3COONa + H2O + CO2(g)</text>
    <text x="595" y="125" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">CO2 gas forms white precipitate with limewater</text>

    <!-- 3. Neutralization with Bases -->
    <rect x="0" y="180" width="370" height="180" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="185" y="208" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. Neutralization with Alkalis &amp; Bases</text>
    <rect x="15" y="225" width="340" height="120" fill="#0f172a" rx="6"/>
    <text x="185" y="250" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">CH3COOH + NaOH --&gt; CH3COONa + H2O</text>
    <text x="185" y="275" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">2CH3COOH + CuO --&gt; (CH3COO)2Cu + H2O</text>
    <text x="185" y="305" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Classic Acid + Base --&gt; Salt + Water</text>
    <text x="185" y="328" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Forms blue copper(II) ethanoate solution with CuO</text>

    <!-- 4. Fischer Esterification -->
    <rect x="410" y="180" width="370" height="180" fill="#1e293b" rx="10" stroke="#f472b6" stroke-width="2"/>
    <text x="595" y="208" fill="#f472b6" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4. Fischer Esterification (Sweet Esters)</text>
    <rect x="425" y="225" width="340" height="120" fill="#0f172a" rx="6"/>
    <text x="595" y="250" fill="#f472b6" font-family="monospace" font-size="11" text-anchor="middle">CH3COOH + C2H5OH &lt;==[Conc H2SO4]==&gt; CH3COOC2H5 + H2O</text>
    <text x="595" y="275" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Ethanoic Acid + Ethanol &lt;==&gt; <tspan fill="#facc15" font-weight="bold">Ethyl Ethanoate</tspan> + Water</text>
    <text x="595" y="305" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Reversible condensation reaction warmed in water bath</text>
    <text x="595" y="328" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Sweet fruity aroma; forms immiscible oily top layer</text>
  </g>
</svg>"""
    create_or_update_svg_block(l127, 5, 'Chemical Properties of Alkanoic Acids: Metals, Carbonates, Bases, and Fischer Esterification', 'alkanoic_chemical_reactions_127', svg_127)
    print()

    # =========================================================================
    # LESSON 128: Uses of Alkanoic Acids
    # =========================================================================
    l128 = Lesson.objects.get(id=128)
    print(f'Enriching Lesson 128: \"{l128.title}\"')
    create_or_update_wm_block(
        l128, 2, 'Traditional Pickled Food Preservation in Dilute Aqueous Ethanoic Acid (Vinegar)',
        'Pickled_vegetables_jars.jpg', 'Rainer Zenz', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Pickled_vegetables_jars.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l128, 3, 'Synthetic Cellulose Acetate Fibre Fabrics and Commercial Solvent Reagent Bottles',
        'Cellulose_acetate_fibers.jpg', 'Rama', 'CeCILL',
        'https://commons.wikimedia.org/wiki/File:Cellulose_acetate_fibers.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_128 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Five Major Industrial &amp; Domestic Applications of Alkanoic Acids</text>

  <g transform="translate(40, 65)">
    <!-- 1. Food Preservation -->
    <rect x="0" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Food &amp; Preservatives</text>
    <rect x="15" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="122" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Vinegar (4-8% Ethanoic Acid)</text>
    <text x="122" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Pickling vegetables &amp; meat</text>
    <text x="122" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Lowers pH to kill food microbes</text>
    <text x="122" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Sodium benzoate food additive</text>

    <!-- 2. Esters & Flavorings -->
    <rect x="270" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#f472b6" stroke-width="2"/>
    <text x="392" y="28" fill="#f472b6" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Esters &amp; Perfumes</text>
    <rect x="285" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="392" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Fruity Esters Synthesis</text>
    <text x="392" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Ethyl ethanoate (pear/banana drops)</text>
    <text x="392" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Octyl ethanoate (orange flavour)</text>
    <text x="392" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Perfumes &amp; cosmetic fragrances</text>

    <!-- 3. Synthetic Fibres -->
    <rect x="540" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="662" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. Synthetic Fibres &amp; Plastics</text>
    <rect x="555" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="662" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Cellulose Acetate &amp; PVA</text>
    <text x="662" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Rayon artificial silk fabrics</text>
    <text x="662" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Photographic film bases</text>
    <text x="662" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Polyvinyl acetate (wood adhesives)</text>

    <!-- 4. Pharmaceuticals -->
    <rect x="135" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="257" y="218" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4. Pharmaceuticals &amp; Drugs</text>
    <rect x="150" y="235" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="257" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Aspirin &amp; Painkillers</text>
    <text x="257" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Acetylsalicylic acid (Aspirin)</text>
    <text x="257" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Acetylation of salicylic acid</text>
    <text x="257" y="320" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Paracetamol drug synthesis</text>

    <!-- 5. Coagulation & Leather -->
    <rect x="405" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#a78bfa" stroke-width="2"/>
    <text x="527" y="218" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">5. Rubber &amp; Leather Industry</text>
    <rect x="420" y="235" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="527" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Latex Coagulation &amp; Tanning</text>
    <text x="527" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Methanoic acid coagulates latex</text>
    <text x="527" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Leather tanning and dyeing</text>
    <text x="527" y="320" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Textile finishing descaler</text>
  </g>
</svg>"""
    create_or_update_svg_block(l128, 4, 'Five Key Application Domains of Alkanoic Acids in Food, Esters, Plastics, Drugs, and Rubber', 'alkanoic_uses_matrix_128', svg_128)
    print()

    print('=== First Half of Topic 6 (Lessons 117 - 128) Completed Successfully! ===')

if __name__ == '__main__':
    enrich_topic6_first_half()
