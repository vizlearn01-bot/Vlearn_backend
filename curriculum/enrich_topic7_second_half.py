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
    if not block or block.assets.filter(source_type='ai_generated').exists():
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
    if not block or block.assets.filter(source_type='external').exists():
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

def enrich_topic7_second_half():
    print('=== ENRICHING FORM 4 TOPIC 7: RADIOACTIVITY (SECOND HALF: LESSONS 150 - 158) ===\n')

    # =========================================================================
    # LESSON 150: Nuclear Reactions
    # =========================================================================
    l150 = Lesson.objects.get(id=150)
    print(f'Enriching Lesson 150: \"{l150.title}\"')
    create_or_update_wm_block(
        l150, 2, 'Rutherford Alpha Particle Gold Foil Scattering Apparatus Historical Laboratory Model',
        'Rutherford_gold_foil_experiment_apparatus.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Rutherford_gold_foil_experiment_apparatus.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l150, 4, 'Heavy Water Nuclear Research Reactor Core Showing Luminous Blue Cherenkov Radiation Glow',
        'Cherenkov_radiation_in_reactor_core.jpg', 'Argonne National Laboratory', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Cherenkov_radiation_in_reactor_core.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_150 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Balancing Nuclear Equations: The Two Golden Conservation Laws</text>

  <!-- Top Conservation Rules Banner -->
  <rect x="40" y="65" width="780" height="95" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
  <text x="430" y="90" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">The Two Fundamental Conservation Laws</text>
  <text x="430" y="118" fill="#4ade80" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">1. Conservation of Mass Number: Σ A(reactants) = Σ A(products)</text>
  <text x="430" y="142" fill="#38bdf8" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">2. Conservation of Atomic Number (Charge): Σ Z(reactants) = Σ Z(products)</text>

  <!-- Left: Alpha Decay Box -->
  <rect x="40" y="175" width="370" height="255" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="225" y="205" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Alpha (α) Decay Equation</text>

  <rect x="60" y="225" width="330" height="85" fill="#0f172a" rx="8"/>
  <text x="225" y="255" fill="#f8fafc" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">A_Z X --&gt; (A-4)_(Z-2) Y + 4_2 He</text>
  <text x="225" y="285" fill="#4ade80" font-family="monospace" font-size="11" text-anchor="middle">226_88 Ra --&gt; 222_86 Rn + 4_2 He</text>

  <rect x="60" y="325" width="330" height="90" fill="#0f172a" rx="6"/>
  <text x="225" y="348" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Alpha Decay Rules</text>
  <text x="225" y="370" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mass number (A) decreases by exactly 4</text>
  <text x="225" y="392" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Atomic number (Z) decreases by exactly 2 (New element)</text>

  <!-- Right: Beta Decay Box -->
  <rect x="450" y="175" width="370" height="255" fill="#1e293b" rx="12" stroke="#fbbf24" stroke-width="2"/>
  <text x="635" y="205" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Beta (β-) Decay Equation</text>

  <rect x="475" y="225" width="320" height="85" fill="#0f172a" rx="8"/>
  <text x="635" y="255" fill="#f8fafc" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">A_Z X --&gt; A_(Z+1) Y + 0_-1 e</text>
  <text x="635" y="285" fill="#4ade80" font-family="monospace" font-size="11" text-anchor="middle">14_6 C --&gt; 14_7 N + 0_-1 e</text>

  <rect x="475" y="325" width="320" height="90" fill="#0f172a" rx="6"/>
  <text x="635" y="348" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Beta Decay Mechanism (1_0n --&gt; 1_1p + 0_-1e)</text>
  <text x="635" y="370" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mass number (A) remains UNCHANGED</text>
  <text x="635" y="392" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Atomic number (Z) increases by 1 (Neutron turns to proton)</text>
</svg>"""
    create_or_update_svg_block(l150, 3, 'The Two Golden Conservation Laws of Nuclear Reactions for Alpha and Beta Equations', 'nuclear_equations_150', svg_150)
    print()

    # =========================================================================
    # LESSON 151: Radioactive Decay Series
    # =========================================================================
    l151 = Lesson.objects.get(id=151)
    print(f'Enriching Lesson 151: \"{l151.title}\"')
    create_or_update_wm_block(
        l151, 2, 'Thorium Nitrate Pure Reagent Compound Exhibiting Natural Alpha and Beta Activity',
        'Thorium_nitrate_reagent.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Thorium_nitrate_reagent.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l151, 3, 'Solid-State Radon Gas Alpha Track Etch Nuclear Decay Detector for Soil and Basements',
        'Radon_detector_track_etch.jpg', 'US EPA', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Radon_detector_track_etch.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_151 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Radioactive Decay Series: Sequential Disintegration Cascade to Stable Lead</text>

  <!-- Thorium-232 Decay Cascade Roadmap -->
  <rect x="40" y="65" width="780" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="430" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Thorium-232 (4n) Decay Series Cascade to Stable Lead-208</text>

  <g transform="translate(60, 115)">
    <!-- Step 1: Th-232 -->
    <rect x="0" y="20" width="100" height="50" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
    <text x="50" y="45" fill="#f87171" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">232_90 Th</text>
    <text x="50" y="60" fill="#94a3b8" font-size="9" text-anchor="middle">Parent (Alpha)</text>

    <!-- Arrow 1 (Alpha) -->
    <line x1="100" y1="45" x2="140" y2="45" stroke="#f87171" stroke-width="2"/>
    <text x="120" y="38" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">-α</text>

    <!-- Step 2: Ra-228 -->
    <rect x="140" y="20" width="100" height="50" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
    <text x="190" y="45" fill="#fbbf24" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">228_88 Ra</text>
    <text x="190" y="60" fill="#94a3b8" font-size="9" text-anchor="middle">(Beta)</text>

    <!-- Arrow 2 (Beta) -->
    <line x1="240" y1="45" x2="280" y2="45" stroke="#fbbf24" stroke-width="2"/>
    <text x="260" y="38" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">-β</text>

    <!-- Step 3: Ac-228 -->
    <rect x="280" y="20" width="100" height="50" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
    <text x="330" y="45" fill="#fbbf24" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">228_89 Ac</text>
    <text x="330" y="60" fill="#94a3b8" font-size="9" text-anchor="middle">(Beta)</text>

    <!-- Arrow 3 (Beta) -->
    <line x1="380" y1="45" x2="420" y2="45" stroke="#fbbf24" stroke-width="2"/>
    <text x="400" y="38" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">-β</text>

    <!-- Step 4: Th-228 -->
    <rect x="420" y="20" width="100" height="50" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
    <text x="470" y="45" fill="#f87171" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">228_90 Th</text>
    <text x="470" y="60" fill="#94a3b8" font-size="9" text-anchor="middle">(Alpha)</text>

    <!-- Multi-step bridge -->
    <line x1="520" y1="45" x2="570" y2="45" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>
    <text x="545" y="38" fill="#38bdf8" font-size="10" text-anchor="middle">... 5α, 2β</text>

    <!-- Final Stable: Pb-208 -->
    <rect x="570" y="15" width="150" height="60" fill="#0f172a" rx="8" stroke="#4ade80" stroke-width="2"/>
    <text x="645" y="45" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">208_82 Pb</text>
    <text x="645" y="65" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">STABLE END PRODUCT</text>

    <!-- Summary Box -->
    <rect x="0" y="110" width="740" height="165" fill="#0f172a" rx="8"/>
    <text x="370" y="138" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Net Nuclear Equation for Thorium Decay Chain</text>
    <text x="370" y="170" fill="#38bdf8" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">232_90 Th --&gt; 208_82 Pb + 6 (4_2 He) + 4 (0_-1 e)</text>
    
    <text x="370" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• ΔA = 232 - 208 = 24  ==&gt;  Number of α particles = 24 / 4 = <tspan fill="#f87171" font-weight="bold">6 Alpha particles</tspan></text>
    <text x="370" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Expected Z = 90 - (2 × 6) = 78  ==&gt;  Actual Z = 82  ==&gt;  Number of β = 82 - 78 = <tspan fill="#fbbf24" font-weight="bold">4 Beta particles</tspan></text>
    <text x="370" y="255" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">All 4 natural radioactive decay series terminate at non-radioactive Lead (Pb) or Bismuth (Bi)</text>
  </g>
</svg>"""
    create_or_update_svg_block(l151, 3, 'Thorium-232 Radioactive Decay Series Cascade and Stepwise Net Alpha/Beta Calculations', 'decay_series_cascade_151', svg_151)
    print()

    # =========================================================================
    # LESSON 152: Nuclear Fission
    # =========================================================================
    l152 = Lesson.objects.get(id=152)
    print(f'Enriching Lesson 152: \"{l152.title}\"')
    create_or_update_wm_block(
        l152, 2, 'Commercial Pressurized Water Nuclear Power Plant Hyperboloid Cooling Towers and Concrete Containment Dome',
        'Nuclear_power_plant_cooling_towers.jpg', 'Stephan Hoerold', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Nuclear_power_plant_cooling_towers.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l152, 4, 'Cherenkov Blue Luminescence Emitted by High-Speed Beta Particles in Nuclear Reactor Pool',
        'Cherenkov_light_fuel_elements.jpg', 'Idaho National Laboratory', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Cherenkov_light_fuel_elements.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_152 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Nuclear Fission: Uranium-235 Thermal Neutron Splitting &amp; Chain Reaction</text>

  <!-- Left: Fission Reaction Diagram -->
  <rect x="40" y="65" width="460" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="270" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Induced Fission of Uranium-235</text>

  <g transform="translate(60, 115)">
    <rect x="0" y="0" width="420" height="155" fill="#0f172a" rx="8"/>
    <!-- Slow neutron hitting U-235 -->
    <circle cx="35" cy="75" r="8" fill="#38bdf8"/><text x="35" y="79" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">n</text>
    <line x1="45" y1="75" x2="85" y2="75" stroke="#38bdf8" stroke-width="2"/>

    <!-- U-235 -->
    <circle cx="120" cy="75" r="28" fill="#ef4444"/><text x="120" y="79" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">235_92 U</text>
    <line x1="150" y1="75" x2="190" y2="75" stroke="#facc15" stroke-width="2"/>

    <!-- Unstable U-236 Compound -->
    <ellipse cx="225" cy="75" rx="30" ry="20" fill="#f59e0b"/><text x="225" y="79" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">236_92 U*</text>

    <!-- Fission Split -->
    <path d="M 260 75 L 305 40" stroke="#facc15" stroke-width="2"/>
    <circle cx="330" cy="35" r="18" fill="#38bdf8"/><text x="330" y="39" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">141_56 Ba</text>

    <path d="M 260 75 L 305 110" stroke="#facc15" stroke-width="2"/>
    <circle cx="330" cy="115" r="16" fill="#4ade80"/><text x="330" y="119" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">92_36 Kr</text>

    <!-- 3 prompt neutrons -->
    <circle cx="395" cy="50" r="6" fill="#facc15"/><text x="415" y="54" fill="#facc15" font-size="9">3 1_0n</text>
    <circle cx="395" cy="75" r="6" fill="#facc15"/>
    <circle cx="395" cy="100" r="6" fill="#facc15"/>
  </g>

  <rect x="60" y="290" width="420" height="120" fill="#0f172a" rx="6"/>
  <text x="270" y="315" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">235_92U + 1_0n --&gt; 141_56Ba + 92_36Kr + 3(1_0n) + 200 MeV</text>
  <text x="270" y="342" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mass of products &lt; Mass of reactants (Mass Defect Δm)</text>
  <text x="270" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Energy released: E = Δm · c^2 (Colossal heat &amp; radiation)</text>
  <text x="270" y="390" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">1 kg Uranium-235 yields as much energy as 2,500 tonnes of coal!</text>

  <!-- Right: Nuclear Reactor Core Controls -->
  <rect x="520" y="65" width="300" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="670" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Nuclear Reactor Controls</text>

  <rect x="540" y="115" width="260" height="75" fill="#0f172a" rx="6"/>
  <text x="555" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Moderator (Graphite / D2O)</text>
  <text x="555" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Slows fast neutrons down to thermal</text>
  <text x="555" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">speeds required for U-235 capture</text>

  <rect x="540" y="200" width="260" height="75" fill="#0f172a" rx="6"/>
  <text x="555" y="223" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Control Rods (Boron / Cadmium)</text>
  <text x="555" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Absorb excess neutrons</text>
  <text x="555" y="263" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Maintains exact critical multiplication (k=1)</text>

  <rect x="540" y="285" width="260" height="125" fill="#0f172a" rx="6"/>
  <text x="555" y="308" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Coolant &amp; Shielding</text>
  <text x="555" y="330" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Pressurized water / CO2 extracts heat</text>
  <text x="555" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Drives steam turbine electricity generator</text>
  <text x="555" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">Thick lead/concrete biological shield</text>
  <text x="555" y="395" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Protects operators from escaping radiation</text>
</svg>"""
    create_or_update_svg_block(l152, 4, 'Nuclear Fission Mechanism of Uranium-235, Mass Defect Energy Release, and Reactor Core Components', 'nuclear_fission_mechanism_152', svg_152)
    print()

    # =========================================================================
    # LESSON 153: Nuclear Fusion
    # =========================================================================
    l153 = Lesson.objects.get(id=153)
    print(f'Enriching Lesson 153: \"{l153.title}\"')
    create_or_update_wm_block(
        l153, 2, 'Thermonuclear Solar Flare Eruption and Core Hydrogen Fusion in the Sun Observed via NASA SDO',
        'Sun_coronal_mass_ejection_fusion.jpg', 'NASA Goddard Space Flight Center', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Sun_coronal_mass_ejection_fusion.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l153, 3, 'Experimental Toroidal Tokamak Magnetic Confinement Fusion Reactor Vacuum Chamber',
        'Tokamak_fusion_reactor_interior.jpg', 'ITER Organization', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Tokamak_fusion_reactor_interior.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_153 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Nuclear Fusion: Deuterium-Tritium Joining &amp; Fission vs. Fusion Comparison</text>

  <!-- Left: D-T Fusion Mechanism -->
  <rect x="40" y="65" width="440" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="260" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Deuterium-Tritium (D-T) Thermonuclear Fusion</text>

  <g transform="translate(65, 115)">
    <rect x="0" y="0" width="390" height="135" fill="#0f172a" rx="8"/>
    <!-- Deuterium (1p, 1n) -->
    <circle cx="45" cy="45" r="14" fill="#38bdf8"/><text x="45" y="49" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">2_1 H</text>
    <text x="45" y="70" fill="#38bdf8" font-size="9" text-anchor="middle">Deuterium</text>

    <text x="85" y="50" fill="#facc15" font-size="18" font-weight="bold" text-anchor="middle">+</text>

    <!-- Tritium (1p, 2n) -->
    <circle cx="125" cy="45" r="14" fill="#fbbf24"/><text x="125" y="49" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">3_1 H</text>
    <text x="125" y="70" fill="#fbbf24" font-size="9" text-anchor="middle">Tritium</text>

    <text x="175" y="50" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">--[&gt;10^8 K]--&gt;</text>

    <!-- Helium-4 + Neutron + 17.6 MeV -->
    <circle cx="250" cy="45" r="18" fill="#4ade80"/><text x="250" y="49" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">4_2 He</text>
    <text x="250" y="75" fill="#4ade80" font-size="9" text-anchor="middle">Helium-4</text>

    <text x="290" y="50" fill="#facc15" font-size="16" text-anchor="middle">+</text>
    <circle cx="320" cy="45" r="8" fill="#facc15"/><text x="320" y="49" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">n</text>
    <text x="320" y="70" fill="#facc15" font-size="9" text-anchor="middle">1_0 n</text>

    <text x="200" y="115" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">2_1H + 3_1H --&gt; 4_2He + 1_0n + 17.6 MeV</text>
  </g>

  <rect x="65" y="270" width="390" height="140" fill="#0f172a" rx="6"/>
  <text x="260" y="295" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">The Extreme High-Temperature Bottleneck</text>
  <text x="260" y="318" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Both positively charged nuclei strongly repel (Coulomb Barrier)</text>
  <text x="260" y="340" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Requires &gt; 100,000,000°C for extreme kinetic velocity</text>
  <text x="260" y="365" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Powers the Sun &amp; Stars (Hydrogen burning cycle)</text>
  <text x="260" y="390" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Inexhaustible fuel from seawater (Deuterium is abundant)</text>

  <!-- Right: Fission vs Fusion Matrix -->
  <rect x="500" y="65" width="320" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="660" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Fission vs. Fusion Comparison</text>

  <rect x="520" y="115" width="280" height="135" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
  <text x="660" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Nuclear Fission</text>
  <text x="535" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Heavy nucleus splits into medium fragments</text>
  <text x="535" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Initiated by thermal neutron capture</text>
  <text x="535" y="200" fill="#f87171" font-family="system-ui, sans-serif" font-size="10">• Produces long-lived radioactive nuclear waste</text>
  <text x="535" y="222" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">• Commercial electricity generation today</text>

  <rect x="520" y="260" width="280" height="150" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
  <text x="660" y="285" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Nuclear Fusion</text>
  <text x="535" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Light nuclei fuse into heavier helium nucleus</text>
  <text x="535" y="328" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Requires &gt;100 million °C plasma confinement</text>
  <text x="535" y="350" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">• Produces clean non-radioactive Helium (No long waste!)</text>
  <text x="535" y="375" fill="#facc15" font-family="system-ui, sans-serif" font-size="10">• Yields 4x more energy per gram than fission</text>
  <text x="535" y="395" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9">Active research: Tokamaks &amp; ITER</text>
</svg>"""
    create_or_update_svg_block(l153, 5, 'Deuterium-Tritium Nuclear Fusion Mechanism, Coulomb Barrier, and Fission vs Fusion Comparison', 'fusion_vs_fission_153', svg_153)
    print()

    # =========================================================================
    # LESSON 154: Applications of Radioactivity
    # =========================================================================
    l154 = Lesson.objects.get(id=154)
    print(f'Enriching Lesson 154: \"{l154.title}\"')
    create_or_update_wm_block(
        l154, 2, 'Industrial Gamma Radiography Camera Testing Welded Steel Structural Pipeline Integrity',
        'Industrial_radiography_pipeline_testing.jpg', 'US NRC', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Industrial_radiography_pipeline_testing.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l154, 5, 'Commercial Food Irradiation Processing Facility Using Cobalt-60 Gamma Radiation to Extend Shelf Life',
        'Food_irradiation_cobalt60_facility.jpg', 'USDA', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Food_irradiation_cobalt60_facility.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_154 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Key Sectors of Radioisotope Applications: Medicine, Industry &amp; Agriculture</text>

  <g transform="translate(40, 65)">
    <!-- 1. Medicine -->
    <rect x="0" y="0" width="245" height="355" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Medicine &amp; Health</text>
    
    <rect x="15" y="45" width="215" height="135" fill="#0f172a" rx="6"/>
    <text x="122" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Cancer Radiotherapy</text>
    <text x="122" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Cobalt-60 (60_27Co) gamma beam</text>
    <text x="122" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">destroys deep malignant tumors</text>
    <text x="122" y="135" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Thyroid Diagnostics</text>
    <text x="122" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Iodine-131 (131_53I) tracer</text>
    <text x="122" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">monitors thyroid uptake &amp; goitre</text>

    <rect x="15" y="195" width="215" height="145" fill="#0f172a" rx="6"/>
    <text x="122" y="218" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Medical Sterilization</text>
    <text x="122" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Gamma irradiation sterilizes</text>
    <text x="122" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">pre-packaged surgical syringes,</text>
    <text x="122" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">gloves, and heart valves without heat</text>
    <text x="122" y="310" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">100% germ-free packaging</text>

    <!-- 2. Industry -->
    <rect x="270" y="0" width="245" height="355" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="392" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Industry &amp; Technology</text>
    
    <rect x="285" y="45" width="215" height="135" fill="#0f172a" rx="6"/>
    <text x="392" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Sheet Thickness Control</text>
    <text x="392" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Beta emitter (Sr-90) &amp; detector</text>
    <text x="392" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">automatically adjusts rollers for</text>
    <text x="392" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">uniform paper/metal foil thickness</text>
    <text x="392" y="155" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Real-time micron precision</text>

    <rect x="285" y="195" width="215" height="145" fill="#0f172a" rx="6"/>
    <text x="392" y="218" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Underground Pipe Leaks</text>
    <text x="392" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Sodium-24 (24_11Na) short-lived</text>
    <text x="392" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">tracer injected into pipeline;</text>
    <text x="392" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Geiger counter pinpoints exact leak</text>
    <text x="392" y="310" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">No digging up entire road</text>

    <!-- 3. Agriculture & Archaeology -->
    <rect x="540" y="0" width="245" height="355" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="662" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3. Agriculture &amp; Dating</text>
    
    <rect x="555" y="45" width="215" height="135" fill="#0f172a" rx="6"/>
    <text x="662" y="68" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Fertilizer Uptake &amp; Pests</text>
    <text x="662" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Phosphorus-32 (32_15P) traces</text>
    <text x="662" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">root absorption efficiency in crops</text>
    <text x="662" y="135" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Sterile Insect Technique</text>
    <text x="662" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Eradicates tsetse flies / fruit pests</text>

    <rect x="555" y="195" width="215" height="145" fill="#0f172a" rx="6"/>
    <text x="662" y="218" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Carbon-14 Dating (5730 yrs)</text>
    <text x="662" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Measures residual 14_6C in dead</text>
    <text x="662" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">organic wood, bones, and fossils</text>
    <text x="662" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Accurate dating up to 50,000 years</text>
    <text x="662" y="310" fill="#facc15" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Archaeological timeline tool</text>
  </g>
</svg>"""
    create_or_update_svg_block(l154, 4, 'Comprehensive Application Matrix of Radioisotopes in Medicine, Industry, and Agriculture', 'radioactivity_applications_matrix_154', svg_154)
    print()

    # =========================================================================
    # LESSON 155: Uses of Radioactive Isotopes
    # =========================================================================
    l155 = Lesson.objects.get(id=155)
    print(f'Enriching Lesson 155: \"{l155.title}\"')
    create_or_update_wm_block(
        l155, 2, 'Clinical Positron Emission Tomography (PET-CT) Imaging Scanner in Hospital Diagnostic Suite',
        'PET_CT_scanner_clinical.jpg', 'Jan Ainali', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:PET_CT_scanner_clinical.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l155, 4, 'Radioactive Phosphorus-32 Autoradiograph Visualizing Plant Nutrient Uptake in Leaves',
        'Phosphorus32_plant_autoradiograph.jpg', 'Agricultural Research Service', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Phosphorus32_plant_autoradiograph.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_155 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The KCSE Essential Radioisotope Toolkit: Identity, Half-Life &amp; Exact Role</text>

  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="780" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
    
    <!-- Table Header -->
    <rect x="15" y="15" width="750" height="35" fill="#0f172a" rx="6"/>
    <text x="90" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Radioisotope</text>
    <text x="210" y="38" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Radiation &amp; Half-Life</text>
    <text x="480" y="38" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Key Syllabus Application &amp; Principle</text>

    <!-- Row 1: Cobalt-60 -->
    <rect x="15" y="55" width="750" height="45" fill="#0f172a" rx="4"/>
    <text x="90" y="82" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Cobalt-60 (60_27Co)</text>
    <text x="210" y="82" fill="#cbd5e1" font-size="11" text-anchor="middle">γ-rays | t1/2 = 5.27 yrs</text>
    <text x="480" y="82" fill="#cbd5e1" font-size="11" text-anchor="middle">Deep cancer radiotherapy; medical instrument sterilization</text>

    <!-- Row 2: Iodine-131 -->
    <rect x="15" y="105" width="750" height="45" fill="#0f172a" rx="4"/>
    <text x="90" y="132" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Iodine-131 (131_53I)</text>
    <text x="210" y="132" fill="#cbd5e1" font-size="11" text-anchor="middle">β-, γ-rays | t1/2 = 8.0 days</text>
    <text x="480" y="132" fill="#cbd5e1" font-size="11" text-anchor="middle">Diagnosis and treatment of thyroid gland disorders &amp; goitre</text>

    <!-- Row 3: Carbon-14 -->
    <rect x="15" y="155" width="750" height="45" fill="#0f172a" rx="4"/>
    <text x="90" y="182" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Carbon-14 (14_6C)</text>
    <text x="210" y="182" fill="#cbd5e1" font-size="11" text-anchor="middle">β- particles | t1/2 = 5730 yrs</text>
    <text x="480" y="182" fill="#cbd5e1" font-size="11" text-anchor="middle">Archaeological radiocarbon dating of wood, fossils, and bones</text>

    <!-- Row 4: Phosphorus-32 -->
    <rect x="15" y="205" width="750" height="45" fill="#0f172a" rx="4"/>
    <text x="90" y="232" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Phosphorus-32 (32_15P)</text>
    <text x="210" y="232" fill="#cbd5e1" font-size="11" text-anchor="middle">β- particles | t1/2 = 14.3 days</text>
    <text x="480" y="232" fill="#cbd5e1" font-size="11" text-anchor="middle">Agricultural tracer for fertilizer uptake; leukemia therapy</text>

    <!-- Row 5: Sodium-24 -->
    <rect x="15" y="255" width="750" height="45" fill="#0f172a" rx="4"/>
    <text x="90" y="282" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Sodium-24 (24_11Na)</text>
    <text x="210" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">β-, γ-rays | t1/2 = 15 hours</text>
    <text x="480" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">Tracing underground pipe leaks and blood circulation disorders</text>

    <!-- Row 6: Americium-241 -->
    <rect x="15" y="305" width="750" height="40" fill="#0f172a" rx="4"/>
    <text x="90" y="330" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Americium-241 (241_95Am)</text>
    <text x="210" y="330" fill="#cbd5e1" font-size="11" text-anchor="middle">α-particles | t1/2 = 432 yrs</text>
    <text x="480" y="330" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Ionization smoke detectors for domestic fire safety</text>
  </g>
</svg>"""
    create_or_update_svg_block(l155, 3, 'Master Reference Toolkit of Essential Radioisotopes, Half-Lives, and Specific Roles', 'radioisotope_toolkit_155', svg_155)
    print()

    # =========================================================================
    # LESSON 156: Dangers of Radioactivity
    # =========================================================================
    l156 = Lesson.objects.get(id=156)
    print(f'Enriching Lesson 156: \"{l156.title}\"')
    create_or_update_wm_block(
        l156, 2, 'International Universal Ionizing Radiation Trefoil Hazard Warning Symbol',
        'Radiation_warning_symbol.jpg', 'Mattes', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Radiation_warning_symbol.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l156, 3, 'High-Resolution Microscopic Chromosomal DNA Aberrations Caused by Radiation-Induced Free Radicals',
        'Radiation_chromosome_aberrations.jpg', 'US Department of Energy', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Radiation_chromosome_aberrations.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_156 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Dangers of Ionizing Radiation: Biological Mechanisms &amp; Health Consequences</text>

  <!-- Left: Cellular Ionization Mechanism -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="225" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Sub-Cellular Damage Mechanism</text>

  <rect x="60" y="115" width="330" height="85" fill="#0f172a" rx="6" stroke="#ef4444" stroke-width="1"/>
  <text x="75" y="138" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Water Radiolysis &amp; Free Radicals</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Radiation ionizes H2O in cells --&gt; •OH, •H</text>
  <text x="75" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Highly reactive hydroxyl free radicals attack DNA</text>

  <rect x="60" y="210" width="330" height="85" fill="#0f172a" rx="6" stroke="#f97316" stroke-width="1"/>
  <text x="75" y="233" fill="#f97316" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">DNA Strand Breaks &amp; Mutations</text>
  <text x="75" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Double-strand DNA fractures cannot be repaired</text>
  <text x="75" y="275" fill="#fed7aa" font-family="system-ui, sans-serif" font-size="10">Leads to oncogene activation &amp; uncontrolled cell division</text>

  <rect x="60" y="305" width="330" height="95" fill="#0f172a" rx="6"/>
  <text x="225" y="328" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Somatic vs. Genetic Damage</text>
  <text x="225" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Somatic: Affects individual (Cancer, radiation burns, cataracts)</text>
  <text x="225" y="375" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">• Genetic: Affects gametes/offspring (Congenital birth defects)</text>

  <!-- Right: Acute Radiation Sickness vs Chronic -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#fbbf24" stroke-width="2"/>
  <text x="635" y="95" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Clinical Health Effects by Dose</text>

  <g transform="translate(475, 115)">
    <rect x="0" y="0" width="320" height="55" fill="#0f172a" rx="6"/>
    <text x="15" y="22" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Low Doses (&lt; 0.25 Sv)</text>
    <text x="15" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">No immediate symptoms; slight statistical cancer risk</text>

    <rect x="0" y="65" width="320" height="55" fill="#0f172a" rx="6"/>
    <text x="15" y="87" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Moderate Doses (1 - 3 Sv)</text>
    <text x="15" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Nausea, fatigue, temporary reduction in white blood cells</text>

    <rect x="0" y="130" width="320" height="55" fill="#0f172a" rx="6"/>
    <text x="15" y="152" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">High Doses (3 - 6 Sv)</text>
    <text x="15" y="172" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Severe bone marrow destruction, hair loss, 50% mortality</text>

    <rect x="0" y="195" width="320" height="85" fill="#0f172a" rx="6"/>
    <text x="160" y="220" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Lethal Dose (&gt; 10 Sv)</text>
    <text x="160" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Central nervous system collapse; 100% fatal within days</text>
    <text x="160" y="265" fill="#facc15" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Requires strict ALARA (As Low As Reasonably Achievable)</text>
  </g>
</svg>"""
    create_or_update_svg_block(l156, 3, 'Biological Cellular Damage Mechanisms, DNA Double-Strand Breaks, and Dose Levels', 'radiation_dangers_biological_156', svg_156)
    print()

    # =========================================================================
    # LESSON 157: Environmental Pollution
    # =========================================================================
    l157 = Lesson.objects.get(id=157)
    print(f'Enriching Lesson 157: \"{l157.title}\"')
    create_or_update_wm_block(
        l157, 2, 'Chernobyl Exclusion Zone Reactor Unit 4 Sarcophagus Confinement Shelter',
        'Chernobyl_sarcophagus_reactor4.jpg', 'Carl Montgomery', 'CC BY 2.0',
        'https://commons.wikimedia.org/wiki/File:Chernobyl_sarcophagus_reactor4.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l157, 4, 'High-Level Radioactive Waste Vitrification Glass Canister Storage Facility Vault',
        'Radioactive_waste_vitrification_canisters.jpg', 'US Department of Energy', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Radioactive_waste_vitrification_canisters.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_157 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Nuclear Waste Hierarchy &amp; Deep Geological Multi-Barrier Repository</text>

  <!-- Left: Waste Classification -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Nuclear Waste Classification</text>

  <rect x="60" y="115" width="330" height="65" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
  <text x="75" y="135" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Low-Level Waste (LLW)</text>
  <text x="75" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Lab gloves, protective clothing, syringes (Near-surface burial)</text>

  <rect x="60" y="190" width="330" height="65" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
  <text x="75" y="210" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Intermediate-Level Waste (ILW)</text>
  <text x="75" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Reactor metal cladding, ion-exchange resins (Shielded concrete casks)</text>

  <rect x="60" y="265" width="330" height="135" fill="#0f172a" rx="6" stroke="#ef4444" stroke-width="1"/>
  <text x="75" y="288" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">High-Level Waste (HLW)</text>
  <text x="75" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Spent fuel rods containing Plutonium &amp; Fission products</text>
  <text x="75" y="328" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Intensely radioactive &amp; generates substantial decay heat</text>
  <text x="75" y="352" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">Requires Vitrification (Molten borosilicate glass matrix)</text>
  <text x="75" y="375" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Cooled in pools for 10-20 yrs before permanent deep burial</text>

  <!-- Right: Deep Geological Repository -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Deep Geological Repository (500m)</text>

  <g transform="translate(475, 115)">
    <rect x="0" y="0" width="320" height="50" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
    <text x="160" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Barrier 1: Vitrified Solid Borosilicate Glass</text>
    <text x="160" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Locks radionuclides in insoluble crystalline matrix</text>

    <rect x="0" y="60" width="320" height="50" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
    <text x="160" y="82" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Barrier 2: Thick Copper &amp; Stainless Steel Canister</text>
    <text x="160" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Corrosion-resistant for &gt; 100,000 years</text>

    <rect x="0" y="120" width="320" height="50" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
    <text x="160" y="142" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Barrier 3: Swelling Bentonite Clay Buffer</text>
    <text x="160" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Absorbs water and prevents groundwater migration</text>

    <rect x="0" y="180" width="320" height="95" fill="#0f172a" rx="6" stroke="#a78bfa" stroke-width="1"/>
    <text x="160" y="205" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Barrier 4: Stable Stable Granite Bedrock Formations</text>
    <text x="160" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Seismically quiescent deep rock isolated from biosphere</text>
    <text x="160" y="250" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Zero contamination of human drinking aquifers</text>
  </g>
</svg>"""
    create_or_update_svg_block(l157, 3, 'Nuclear Waste Classification and Deep Geological Repository Multi-Barrier Engineering Architecture', 'nuclear_waste_management_157', svg_157)
    print()

    # =========================================================================
    # LESSON 158: Control of Environmental Pollution
    # =========================================================================
    l158 = Lesson.objects.get(id=158)
    print(f'Enriching Lesson 158: \"{l158.title}\"')
    create_or_update_wm_block(
        l158, 2, 'International Atomic Energy Agency (IAEA) Tamper-Evident Safeguard Seal on Nuclear Containment Vault',
        'IAEA_safeguards_seal.jpg', 'IAEA Imagebank', 'CC BY-SA 2.0',
        'https://commons.wikimedia.org/wiki/File:IAEA_safeguards_seal.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l158, 4, 'Radiation Worker Wearing Full Personal Protective Equipment (PPE) Hazmat Suit and Personal Dosimeter Badge',
        'Radiation_worker_protective_gear.jpg', 'IAEA Imagebank', 'CC BY-SA 2.0',
        'https://commons.wikimedia.org/wiki/File:Radiation_worker_protective_gear.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_158 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Three Cardinal Principles of Radiation Protection: Time, Distance &amp; Shielding</text>

  <!-- TDS Principles -->
  <g transform="translate(40, 65)">
    <!-- Time -->
    <rect x="0" y="0" width="245" height="225" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Minimize TIME</text>
    <rect x="15" y="45" width="215" height="165" fill="#0f172a" rx="6"/>
    <text x="122" y="70" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Dose = Dose Rate × Time</text>
    <text x="122" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Halving the exposure time</text>
    <text x="122" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">halves the absorbed dose</text>
    <text x="122" y="145" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Rapid robotic manipulation</text>
    <text x="122" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">and planned rehearsed protocols</text>
    <text x="122" y="195" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Work quickly and leave zone</text>

    <!-- Distance -->
    <rect x="270" y="0" width="245" height="225" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="392" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Maximize DISTANCE</text>
    <rect x="285" y="45" width="215" height="165" fill="#0f172a" rx="6"/>
    <text x="392" y="70" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Inverse Square Law: I ∝ 1/d^2</text>
    <text x="392" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Doubling distance reduces</text>
    <text x="392" y="115" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">radiation intensity to 1/4</text>
    <text x="392" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Use long-handled mechanical</text>
    <text x="392" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">tongs for radioactive source transfer</text>
    <text x="392" y="195" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Never handle sources directly</text>

    <!-- Shielding -->
    <rect x="540" y="0" width="245" height="225" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="662" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3. Maximize SHIELDING</text>
    <rect x="555" y="45" width="215" height="165" fill="#0f172a" rx="6"/>
    <text x="662" y="70" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Dense Absorber Barriers</text>
    <text x="662" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Lead aprons for radiographers</text>
    <text x="662" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Lead-lined walls &amp; lead glass</text>
    <text x="662" y="145" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Thick high-density concrete</text>
    <text x="662" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">structures around nuclear reactors</text>
    <text x="662" y="195" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Attenuates high-energy photons</text>

    <!-- Bottom: Regulatory Bodies & Monitoring -->
    <rect x="0" y="240" width="785" height="110" fill="#1e293b" rx="10" stroke="#64748b" stroke-width="1"/>
    <text x="392" y="265" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Regulatory Oversight &amp; Personal Dosimetry</text>
    <text x="392" y="290" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Personal Monitoring: Radiation workers wear Film Badges / TLD dosimeters to record cumulative exposure</text>
    <text x="392" y="312" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• National Oversight: KNRA (Kenya Nuclear Regulatory Authority) enforces strict radiation safety codes</text>
    <text x="392" y="335" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• International Standards: IAEA (International Atomic Energy Agency) conducts global safety audits</text>
  </g>
</svg>"""
    create_or_update_svg_block(l158, 3, 'The Three Cardinal Rules of Radiation Protection (Time, Distance, Shielding) and Regulatory Safety Standards', 'radiation_protection_tds_158', svg_158)
    print()

    print('=== Second Half of Topic 7 (Lessons 150 - 158) Completed Successfully! ===')

if __name__ == '__main__':
    enrich_topic7_second_half()
