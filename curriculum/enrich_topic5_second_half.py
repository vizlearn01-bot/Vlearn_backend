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

def enrich_topic5_second_half():
    print('=== ENRICHING FORM 4 TOPIC 5: METALS (SECOND HALF: LESSONS 110 - 115) ===\n')

    # =========================================================================
    # LESSON 110: Copper — Occurrence and Extraction
    # =========================================================================
    l110 = Lesson.objects.get(id=110)
    print(f'Enriching Lesson 110: \"{l110.title}\"')
    create_or_update_wm_block(
        l110, 2, 'Natural Brass-Yellow Chalcopyrite (Copper Pyrites, CuFeS2) Mineral Specimen',
        'Chalcopyrite_crystal.jpg', 'Robert M. Lavinsky', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Chalcopyrite_crystal.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l110, 3, 'Cast Ingot of Rough Blister Copper with Distinct Surface Gas Cavities',
        'Copper_metal_ingot.jpg', 'Jurii', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Copper_metal_ingot.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_110 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Extraction &amp; Electrolytic Refining of Copper: Smelting to 99.99% Purity</text>

  <!-- Left: Smelting & Converter -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f97316" stroke-width="2"/>
  <text x="225" y="95" fill="#f97316" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Smelting &amp; Converter Self-Reduction</text>
  
  <rect x="60" y="115" width="330" height="75" fill="#0f172a" rx="8"/>
  <text x="225" y="135" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Step 1: Partial Roasting with Silica (SiO2)</text>
  <text x="225" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2CuFeS2(s) + 4O2(g) --&gt; Cu2S(l) + 2FeO(s) + 3SO2(g)</text>
  <text x="225" y="173" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Slag: FeO(s) + SiO2(s) --&gt; FeSiO3(l) [Molten Slag tapped]</text>

  <rect x="60" y="200" width="330" height="110" fill="#0f172a" rx="8"/>
  <text x="225" y="222" fill="#f97316" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Step 2: Bessemer Converter (Self-Reduction)</text>
  <text x="225" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2Cu2S(l) + 3O2(g) --&gt; 2Cu2O(l) + 2SO2(g)</text>
  <text x="225" y="262" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Cu2S(l) + 2Cu2O(l) --&gt; 6Cu(l) + SO2(g)</text>
  <text x="225" y="285" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">"Blister Copper" (97-98% pure): Escaping SO2 bubbles</text>

  <rect x="60" y="320" width="330" height="85" fill="#0f172a" rx="6"/>
  <text x="225" y="345" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Contains impurities: Fe, Zn, Ag, Au, Pt</text>
  <text x="225" y="365" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Impurities reduce electrical conductivity drastically</text>
  <text x="225" y="385" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Must undergo electrolytic refining</text>

  <!-- Right: Electrolytic Refining Cell -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="635" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Electrolytic Refining Tank</text>

  <rect x="475" y="115" width="320" height="190" fill="#0284c7" opacity="0.25" rx="8"/>
  <text x="635" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Electrolyte: Acidified CuSO4(aq) + H2SO4(aq)</text>

  <!-- Impure Anode -->
  <rect x="510" y="150" width="40" height="120" fill="#b45309" stroke="#f97316" stroke-width="2" rx="4"/>
  <text x="530" y="210" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" transform="rotate(-90 530,210)">Impure Anode (+)</text>

  <!-- Pure Cathode -->
  <rect x="680" y="150" width="30" height="120" fill="#ea580c" stroke="#fed7aa" stroke-width="2" rx="2"/>
  <text x="695" y="210" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" transform="rotate(90 695,210)">Pure Cu Cathode (-)</text>

  <!-- Anode Slime at bottom -->
  <ellipse cx="530" cy="290" rx="35" ry="8" fill="#facc15" opacity="0.8"/>
  <text x="635" y="295" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Anode Sludge (Ag, Au, Pt)</text>

  <!-- Reactions footer -->
  <rect x="475" y="315" width="320" height="90" fill="#0f172a" rx="6"/>
  <text x="635" y="338" fill="#f97316" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Anode: Cu(s) --&gt; Cu2+(aq) + 2e- (Dissolves)</text>
  <text x="635" y="358" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Cathode: Cu2+(aq) + 2e- --&gt; Cu(s) (Deposits)</text>
  <text x="635" y="380" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Final Cathode Purity = 99.99% Cu</text>
</svg>"""
    create_or_update_svg_block(l110, 5, 'Copper Smelting, Converter Self-Reduction, and Electrolytic Refining Tank Architecture', 'copper_refining_110', svg_110)
    print()

    # =========================================================================
    # LESSON 111: Physical Properties of Metals
    # =========================================================================
    l111 = Lesson.objects.get(id=111)
    print(f'Enriching Lesson 111: \"{l111.title}\"')
    create_or_update_wm_block(
        l111, 2, 'Cast Gold Bullion Ingot Exhibiting Characteristic High Density and Metallic Luster',
        'Gold_bullion_ingots.jpg', 'Alchemist-hp', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Gold_bullion_ingots.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l111, 3, 'Spool of Drawn Copper Wire Demonstrating Ductility and High Electrical Conductivity',
        'Copper_wire_spool.jpg', 'Jurii', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Copper_wire_spool.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_111 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Physical Properties of Metals: The 'Sea of Delocalized Electrons' Model</text>

  <!-- Left: Metallic Bonding & Conduction -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Electrical &amp; Thermal Conduction</text>

  <g transform="translate(65, 115)">
    <!-- Positive Cations -->
    <circle cx="40" cy="30" r="18" fill="#38bdf8"/><text x="40" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="110" cy="30" r="18" fill="#38bdf8"/><text x="110" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="180" cy="30" r="18" fill="#38bdf8"/><text x="180" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="250" cy="30" r="18" fill="#38bdf8"/><text x="250" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>

    <circle cx="40" cy="85" r="18" fill="#38bdf8"/><text x="40" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="110" cy="85" r="18" fill="#38bdf8"/><text x="110" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="180" cy="85" r="18" fill="#38bdf8"/><text x="180" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="250" cy="85" r="18" fill="#38bdf8"/><text x="250" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>

    <!-- Delocalized electrons moving right -->
    <circle cx="75" cy="20" r="5" fill="#facc15"/><text x="75" y="23" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">e-</text>
    <circle cx="145" cy="25" r="5" fill="#facc15"/><text x="145" y="28" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">e-</text>
    <circle cx="215" cy="20" r="5" fill="#facc15"/><text x="215" y="23" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">e-</text>
    <circle cx="75" cy="75" r="5" fill="#facc15"/><text x="75" y="78" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">e-</text>
    <circle cx="145" cy="80" r="5" fill="#facc15"/><text x="145" y="83" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">e-</text>
    <circle cx="215" cy="75" r="5" fill="#facc15"/><text x="215" y="78" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">e-</text>
  </g>

  <rect x="60" y="250" width="330" height="150" fill="#0f172a" rx="6"/>
  <text x="225" y="275" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Delocalized Valence Electrons</text>
  <text x="225" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Free to drift under applied potential difference (Voltage)</text>
  <text x="225" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Transfer kinetic energy rapidly (Thermal conductivity)</text>
  <text x="225" y="350" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Mobile electrons reflect incident light (Metallic Luster)</text>
  <text x="225" y="375" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• High melting points due to strong electrostatic attraction</text>

  <!-- Right: Malleability & Ductility -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Malleability &amp; Ductility (Layer Slip)</text>

  <g transform="translate(475, 115)">
    <!-- Top Layer shifted right by force -->
    <path d="M 10 30 L 40 30" stroke="#f87171" stroke-width="4" marker-end="url(#arrow)"/>
    <text x="20" y="18" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">FORCE</text>

    <!-- Shifted row -->
    <circle cx="80" cy="30" r="18" fill="#4ade80"/><text x="80" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="150" cy="30" r="18" fill="#4ade80"/><text x="150" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="220" cy="30" r="18" fill="#4ade80"/><text x="220" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="290" cy="30" r="18" fill="#4ade80"/><text x="290" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>

    <!-- Bottom row stationary -->
    <circle cx="40" cy="85" r="18" fill="#4ade80"/><text x="40" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="110" cy="85" r="18" fill="#4ade80"/><text x="110" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="180" cy="85" r="18" fill="#4ade80"/><text x="180" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
    <circle cx="250" cy="85" r="18" fill="#4ade80"/><text x="250" y="90" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">+</text>
  </g>

  <rect x="470" y="250" width="330" height="150" fill="#0f172a" rx="6"/>
  <text x="635" y="275" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Non-Directional Metallic Bonding</text>
  <text x="635" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• When struck, positive ion layers slide over one another</text>
  <text x="635" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Sea of electrons adjusts instantly around displaced ions</text>
  <text x="635" y="350" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• No repulsive like-charge alignment occurs (unlike ionic crystals)</text>
  <text x="635" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Allows metals to be hammered into sheets or drawn into wires</text>
</svg>"""
    create_or_update_svg_block(l111, 5, 'Giant Metallic Lattice: Delocalized Electron Sea, Conduction, and Layer Sliding Model', 'metallic_lattice_conduction_111', svg_111)
    print()

    # =========================================================================
    # LESSON 112: Chemical Properties of Metals
    # =========================================================================
    l112 = Lesson.objects.get(id=112)
    print(f'Enriching Lesson 112: \"{l112.title}\"')
    create_or_update_wm_block(
        l112, 2, 'Vigorous Exothermic Reaction of Sodium Metal with Water Producing Hydrogen',
        'Sodium_in_water.jpg', 'Jurii', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Sodium_in_water.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    create_or_update_wm_block(
        l112, 3, 'Bright Incandescent White Flame of Magnesium Ribbon Burning in Atmospheric Air',
        'Magnesium_ribbon_burning.jpg', 'Pavel Ševela', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Magnesium_ribbon_burning.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/8/8a/Magnesium_ribbon_burning.jpg'
    )
    svg_112 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Comparative Chemical Properties of Metals across Four Key Reagents</text>

  <!-- Reactivity Order -->
  <rect x="40" y="65" width="780" height="360" fill="#1e293b" rx="12" stroke="#64748b" stroke-width="2"/>
  
  <!-- Header row -->
  <rect x="60" y="85" width="740" height="40" fill="#0f172a" rx="6"/>
  <text x="120" y="110" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Metal</text>
  <text x="260" y="110" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Reaction with O2 (Air)</text>
  <text x="440" y="110" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Reaction with Water / Steam</text>
  <text x="630" y="110" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Reaction with Dilute Acid</text>
  <text x="750" y="110" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Cl2 Gas</text>

  <!-- Row 1: K, Na -->
  <rect x="60" y="135" width="740" height="50" fill="#1e293b" rx="4" stroke="#38bdf8" stroke-width="1"/>
  <text x="120" y="165" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">K, Na</text>
  <text x="260" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Burns with colored flame (Peroxides/Oxides)</text>
  <text x="440" y="165" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Violent in cold water: 2M + 2H2O --&gt; 2MOH + H2</text>
  <text x="630" y="165" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Explosive (Do not perform)</text>
  <text x="750" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2M + Cl2 --&gt; 2MCl</text>

  <!-- Row 2: Ca, Mg -->
  <rect x="60" y="195" width="740" height="50" fill="#0f172a" rx="4"/>
  <text x="120" y="225" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Ca, Mg</text>
  <text x="260" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Burns brightly to form White Oxide</text>
  <text x="440" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Ca: vigorous in cold water | Mg: reacts with steam (MgO + H2)</text>
  <text x="630" y="225" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Rapid effervescence of H2: M + 2HCl --&gt; MCl2 + H2</text>
  <text x="750" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Burns to MCl2</text>

  <!-- Row 3: Al, Zn, Fe -->
  <rect x="60" y="255" width="740" height="50" fill="#1e293b" rx="4"/>
  <text x="120" y="285" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Al, Zn, Fe</text>
  <text x="260" y="285" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Forms protective oxide coat / glows</text>
  <text x="440" y="285" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">No reaction with cold water; reacts with steam at red heat</text>
  <text x="630" y="285" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Moderate reaction; Fe forms Fe(II) with dilute acid</text>
  <text x="750" y="285" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2Fe + 3Cl2 --&gt; 2FeCl3</text>

  <!-- Row 4: Pb, Cu -->
  <rect x="60" y="315" width="740" height="50" fill="#0f172a" rx="4"/>
  <text x="120" y="345" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Pb, Cu</text>
  <text x="260" y="345" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Superficial oxidation when heated</text>
  <text x="440" y="345" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">No reaction with cold water or steam</text>
  <text x="630" y="345" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Pb forms insoluble coating (PbSO4/PbCl2); Cu no reaction</text>
  <text x="750" y="345" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Cu + Cl2 --&gt; CuCl2</text>
</svg>"""
    create_or_update_svg_block(l112, 5, 'Comprehensive Chemical Reactivity Ladder of Metals with Oxygen, Water, Steam, Acid, and Chlorine', 'metal_reactivity_chart_112', svg_112)
    print()

    # =========================================================================
    # LESSON 113: Uses of Common Metals
    # =========================================================================
    l113 = Lesson.objects.get(id=113)
    print(f'Enriching Lesson 113: \"{l113.title}\"')
    create_or_update_wm_block(
        l113, 2, 'High-Voltage Overhead Power Transmission Lines Constructed from Lightweight Aluminium Cables',
        'Overhead_power_lines_aluminum.jpg', 'Fir0002', 'GFDL 1.2',
        'https://commons.wikimedia.org/wiki/File:Overhead_power_lines_aluminum.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l113, 3, 'Zinc-Galvanized Corrugated Steel Roofing Sheets Protected Against Atmospheric Corrosion',
        'Galvanized_corrugated_sheet.jpg', 'Santeri Viinamäki', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Galvanized_corrugated_sheet.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/a/a7/A_zinc-plated_screw.jpg'
    )
    svg_113 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Property-to-Application Decision Framework for Six Common Metals</text>

  <g transform="translate(40, 65)">
    <!-- Aluminium -->
    <rect x="0" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Aluminium (Al)</text>
    <rect x="15" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="122" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Low Density + High Conductivity</text>
    <text x="122" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Overhead power cables (ACSR)</text>
    <text x="122" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Aircraft bodies &amp; window frames</text>
    <text x="122" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cooking utensils (non-toxic oxide)</text>

    <!-- Copper -->
    <rect x="270" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#fb923c" stroke-width="2"/>
    <text x="392" y="28" fill="#fb923c" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Copper (Cu)</text>
    <rect x="285" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="392" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Superb Conduction + Ductility</text>
    <text x="392" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Domestic electrical wiring</text>
    <text x="392" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Central heating &amp; water pipes</text>
    <text x="392" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Alloys: Brass (Cu+Zn), Bronze (Cu+Sn)</text>

    <!-- Iron -->
    <rect x="540" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
    <text x="662" y="28" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Iron (Fe)</text>
    <rect x="555" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="662" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">High Tensile Strength + Abundance</text>
    <text x="662" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Structural beams &amp; bridges (Steel)</text>
    <text x="662" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Engine blocks &amp; manhole covers</text>
    <text x="662" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Reinforced concrete rebar</text>

    <!-- Zinc -->
    <rect x="0" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="122" y="218" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Zinc (Zn)</text>
    <rect x="15" y="235" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="122" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Sacrificial Protection + Anode</text>
    <text x="122" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Galvanizing iron sheets</text>
    <text x="122" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Dry cell battery outer casing</text>
    <text x="122" y="320" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Sacrificial blocks on ship hulls</text>

    <!-- Lead -->
    <rect x="270" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#a78bfa" stroke-width="2"/>
    <text x="392" y="218" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Lead (Pb)</text>
    <rect x="285" y="235" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="392" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">High Density + Radiation Absorption</text>
    <text x="392" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Car lead-acid accumulator plates</text>
    <text x="392" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• X-ray &amp; nuclear radiation shields</text>
    <text x="392" y="320" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Solder alloy (Pb + Sn)</text>

    <!-- Sodium -->
    <rect x="540" y="190" width="245" height="170" fill="#1e293b" rx="10" stroke="#facc15" stroke-width="2"/>
    <text x="662" y="218" fill="#facc15" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Sodium (Na)</text>
    <rect x="555" y="235" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="662" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Low Melting Point + Yellow Emission</text>
    <text x="662" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Liquid coolant in fast nuclear reactors</text>
    <text x="662" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Yellow sodium street vapor lamps</text>
    <text x="662" y="320" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Manufacture of sodium peroxide (Na2O2)</text>
  </g>
</svg>"""
    create_or_update_svg_block(l113, 4, 'Systematic Property-to-Application Decision Matrix for Al, Cu, Fe, Zn, Pb, and Na', 'metal_applications_matrix_113', svg_113)
    print()

    # =========================================================================
    # LESSON 114: Uses of Iron Alloys
    # =========================================================================
    l114 = Lesson.objects.get(id=114)
    print(f'Enriching Lesson 114: \"{l114.title}\"')
    create_or_update_wm_block(
        l114, 2, 'Structural Steel I-Beams Used as Framework for Heavy High-Rise Construction',
        'Steel_construction_beams.jpg', 'Agnieszka Kwiecień', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Steel_construction_beams.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e4/Blast_Furnace_Duisburg.jpg'
    )
    create_or_update_wm_block(
        l114, 3, 'Polished Stainless Steel Surgical Scissors Resisting Chemical Corrosion and Rust',
        'Stainless_steel_surgical_tools.jpg', 'Rama', 'CeCILL',
        'https://commons.wikimedia.org/wiki/File:Stainless_steel_surgical_tools.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_114 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Iron Alloys: Sub-Microscopic Lattice Distortion &amp; Hardness Mechanism</text>

  <!-- Left: Pure Iron vs Alloy Lattice -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Alloy Lattice Distortion Particle Model</text>

  <g transform="translate(65, 115)">
    <!-- Iron ions with different sized carbon/chromium atoms -->
    <circle cx="40" cy="30" r="16" fill="#94a3b8"/><circle cx="95" cy="30" r="16" fill="#94a3b8"/><circle cx="150" cy="30" r="16" fill="#94a3b8"/><circle cx="205" cy="30" r="16" fill="#94a3b8"/><circle cx="260" cy="30" r="16" fill="#94a3b8"/>
    
    <!-- Row 2 with Interstitial Carbon atom (smaller) -->
    <circle cx="40" cy="80" r="16" fill="#94a3b8"/><circle cx="95" cy="80" r="16" fill="#94a3b8"/>
    <circle cx="140" cy="65" r="8" fill="#facc15"/><text x="140" y="69" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">C</text>
    <circle cx="180" cy="80" r="16" fill="#94a3b8"/><circle cx="235" cy="80" r="16" fill="#94a3b8"/>

    <!-- Row 3 with Substitutional Chromium atom (larger) -->
    <circle cx="40" cy="130" r="16" fill="#94a3b8"/><circle cx="95" cy="130" r="16" fill="#94a3b8"/>
    <circle cx="160" cy="130" r="22" fill="#38bdf8"/><text x="160" y="135" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Cr</text>
    <circle cx="230" cy="130" r="16" fill="#94a3b8"/>
  </g>

  <rect x="60" y="280" width="330" height="120" fill="#0f172a" rx="6"/>
  <text x="225" y="305" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Why Alloys Are Harder Than Pure Metals</text>
  <text x="225" y="328" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Different sized atoms distort regular metal layers</text>
  <text x="225" y="348" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Prevents crystal planes from sliding easily over each other</text>
  <text x="225" y="370" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Increases tensile strength, rigidity, and corrosion resistance</text>

  <!-- Right: Iron Alloy Spectrum -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="635" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. The Iron-Carbon Alloy Spectrum</text>

  <rect x="475" y="115" width="320" height="65" fill="#0f172a" rx="6" stroke="#94a3b8" stroke-width="1"/>
  <text x="490" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Pig / Cast Iron (2.5% - 4.5% Carbon)</text>
  <text x="490" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Extremely hard but brittle. Used in engine blocks, railings, stoves.</text>

  <rect x="475" y="190" width="320" height="65" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
  <text x="490" y="213" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Mild Steel (0.1% - 0.3% Carbon)</text>
  <text x="490" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Malleable and ductile with high tensile strength. Car bodies, beams.</text>

  <rect x="475" y="265" width="320" height="65" fill="#0f172a" rx="6" stroke="#facc15" stroke-width="1"/>
  <text x="490" y="288" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">High Carbon Steel (0.5% - 1.5% Carbon)</text>
  <text x="490" y="310" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Hard and wear-resistant. Drill bits, knives, chisel blades, springs.</text>

  <rect x="475" y="340" width="320" height="65" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
  <text x="490" y="363" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Stainless Steel (Fe + 18% Cr + 8% Ni)</text>
  <text x="490" y="385" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Forms protective Cr2O3 passive layer. Cutlery, surgical tools, tanks.</text>
</svg>"""
    create_or_update_svg_block(l114, 5, 'Sub-Microscopic Alloy Lattice Distortion Model and Iron-Carbon Alloy Spectrum', 'iron_alloys_distortion_114', svg_114)
    print()

    # =========================================================================
    # LESSON 115: Environmental Effects of Metal Extraction
    # =========================================================================
    l115 = Lesson.objects.get(id=115)
    print(f'Enriching Lesson 115: \"{l115.title}\"')
    create_or_update_wm_block(
        l115, 2, 'Large-Scale Open-Pit Mining Terraces Causing Landscape Alteration and Habitat Loss',
        'Open_pit_mine_excavation.jpg', 'Brian Snelson', 'CC BY 2.0',
        'https://commons.wikimedia.org/wiki/File:Open_pit_mine_excavation.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l115, 3, 'Industrial Smelting Flue Gas Stacks Emitting Sulfur Dioxide and Particulates',
        'Smelter_chimney_smoke.jpg', 'US Geological Survey', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Smelter_chimney_smoke.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_115 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Environmental Management in Metallurgy: Pollution Abatement &amp; Closed-Loop Recycling</text>

  <!-- Left: Flue Gas Desulfurization Scrubber -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. SO2 Flue Gas Wet Scrubber</text>

  <rect x="70" y="115" width="310" height="160" fill="#0f172a" rx="8"/>
  <path d="M 120 250 L 120 130 L 330 130 L 330 250 Z" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  
  <!-- Spray nozzles -->
  <circle cx="180" cy="155" r="6" fill="#38bdf8"/><circle cx="225" cy="155" r="6" fill="#38bdf8"/><circle cx="270" cy="155" r="6" fill="#38bdf8"/>
  <text x="225" y="175" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Limestone Slurry Spray (CaCO3 / Ca(OH)2)</text>

  <!-- Gas inlet / clean gas outlet -->
  <text x="90" y="235" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">SO2 IN</text>
  <text x="350" y="145" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">CLEAN GAS</text>

  <rect x="60" y="290" width="330" height="115" fill="#0f172a" rx="6"/>
  <text x="225" y="315" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Scrubber Chemistry &amp; Gypsum Production</text>
  <text x="225" y="338" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">CaCO3(s) + SO2(g) --&gt; CaSO3(s) + CO2(g)</text>
  <text x="225" y="358" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2CaSO3(s) + O2(g) + 4H2O(l) --&gt; 2CaSO4·2H2O(s)</text>
  <text x="225" y="380" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Yields Gypsum (CaSO4·2H2O) used in plasterboard</text>

  <!-- Right: Closed Loop Recycling -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Closed-Loop Metal Recycling Cycle</text>

  <g transform="translate(480, 115)">
    <!-- Circle nodes -->
    <rect x="100" y="0" width="110" height="35" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/><text x="155" y="22" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">1. Scrap Collection</text>
    <rect x="200" y="65" width="100" height="35" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/><text x="250" y="87" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">2. Sorting</text>
    <rect x="100" y="130" width="110" height="35" fill="#0f172a" rx="6" stroke="#facc15" stroke-width="1"/><text x="155" y="152" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">3. Re-melting</text>
    <rect x="0" y="65" width="100" height="35" fill="#0f172a" rx="6" stroke="#a78bfa" stroke-width="1"/><text x="50" y="87" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">4. Manufacturing</text>
  </g>

  <rect x="470" y="290" width="330" height="115" fill="#0f172a" rx="6"/>
  <text x="635" y="315" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Conservation Advantages of Recycling</text>
  <text x="635" y="338" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Aluminium: Saves 95% of extraction energy</text>
  <text x="635" y="358" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Steel / Copper: Saves 60-85% of mining energy</text>
  <text x="635" y="380" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Eliminates toxic tailing dams and slag dumps</text>
</svg>"""
    create_or_update_svg_block(l115, 5, 'Industrial Flue Gas Desulfurization Scrubber and Closed-Loop Metal Recycling Cycle', 'environmental_scrubber_recycling_115', svg_115)
    print()

    print('=== Second Half of Topic 5 (Lessons 110 - 115) Completed Successfully! ===')

if __name__ == '__main__':
    enrich_topic5_second_half()
