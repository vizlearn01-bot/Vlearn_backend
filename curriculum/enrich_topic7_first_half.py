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

def enrich_topic7_first_half():
    print('=== ENRICHING FORM 4 TOPIC 7: RADIOACTIVITY (FIRST HALF: LESSONS 141 - 149) ===\n')

    # =========================================================================
    # LESSON 141: Stability of Isotopes of Elements
    # =========================================================================
    l141 = Lesson.objects.get(id=141)
    print(f'Enriching Lesson 141: \"{l141.title}\"')
    create_or_update_wm_block(
        l141, 2, 'Natural Pitchblende (Uraninite, UO2) Radioactive Mineral Specimen in Protective Display',
        'Uraninite_specimen.jpg', 'Robert M. Lavinsky', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Uraninite_specimen.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l141, 3, 'Mass Spectrometer Chamber Used to Measure Exact Isotopic Masses and Abundances',
        'Mass_spectrometer_detector.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Mass_spectrometer_detector.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_141 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Nuclear Stability: The Neutron-to-Proton (n/p) Ratio &amp; Stability Belt</text>

  <!-- Left: Stability Belt Graph -->
  <rect x="40" y="65" width="440" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="260" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Nuclear Stability Curve (Neutrons vs Protons)</text>

  <g transform="translate(65, 115)">
    <!-- Axes -->
    <line x1="40" y1="230" x2="380" y2="230" stroke="#94a3b8" stroke-width="2"/>
    <line x1="40" y1="230" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
    <text x="210" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Atomic Number / Protons (Z)</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle" transform="rotate(-90 15,125)">Neutrons (N)</text>

    <!-- N = Z line (reference) -->
    <line x1="40" y1="230" x2="280" y2="30" stroke="#64748b" stroke-width="1" stroke-dasharray="3"/>
    <text x="290" y="35" fill="#64748b" font-family="system-ui, sans-serif" font-size="9">N = Z (Slope = 1.0)</text>

    <!-- Stability Belt (curving upwards) -->
    <path d="M 40 230 Q 150 150 240 70 Q 300 25 340 15" stroke="#4ade80" stroke-width="16" fill="none" opacity="0.6"/>
    <text x="250" y="115" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Stability Belt (Stable Nuclides)</text>

    <!-- Region Above: Beta emission -->
    <circle cx="160" cy="70" r="6" fill="#fbbf24"/>
    <text x="175" y="70" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">n/p too high --&gt; β- decay</text>

    <!-- Region Below: Positron / Alpha -->
    <circle cx="270" cy="180" r="6" fill="#f87171"/>
    <text x="280" y="180" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">n/p too low --&gt; β+ / α</text>

    <!-- Top Heavy Nuclei: Z > 83 (Lead) -->
    <line x1="330" y1="230" x2="330" y2="20" stroke="#ef4444" stroke-width="1" stroke-dasharray="2"/>
    <text x="330" y="245" fill="#ef4444" font-size="9" text-anchor="middle">Z = 83 (Bi)</text>
    <text x="340" y="5" fill="#ef4444" font-size="9" font-weight="bold">All Z &gt; 83 are radioactive (Alpha)</text>
  </g>

  <!-- Right: Stability Rules -->
  <rect x="500" y="65" width="320" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="660" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Key Stability Principles</text>

  <rect x="520" y="115" width="280" height="90" fill="#0f172a" rx="6"/>
  <text x="535" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Light Nuclides (Z ≤ 20)</text>
  <text x="535" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Stable when n/p ratio ≈ 1.0</text>
  <text x="535" y="180" fill="#4ade80" font-family="monospace" font-size="11">12_6C (n/p=1.0), 16_8O (n/p=1.0)</text>
  <text x="535" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Strong nuclear force balances proton repulsion</text>

  <rect x="520" y="215" width="280" height="90" fill="#0f172a" rx="6"/>
  <text x="535" y="238" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Heavy Nuclides (20 &lt; Z ≤ 83)</text>
  <text x="535" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Stable when n/p ratio rises to ≈ 1.5</text>
  <text x="535" y="280" fill="#facc15" font-family="monospace" font-size="11">208_82Pb (126/82 = 1.54)</text>
  <text x="535" y="298" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Extra neutrons act as nuclear 'glue'</text>

  <rect x="520" y="315" width="280" height="100" fill="#0f172a" rx="6"/>
  <text x="535" y="338" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Unstable Heavy Elements (Z &gt; 83)</text>
  <text x="535" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Electrostatic repulsion exceeds strong force</text>
  <text x="535" y="380" fill="#fca5a5" font-family="monospace" font-size="11">238_92U (146/92 = 1.59)</text>
  <text x="535" y="402" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">Undergoes spontaneous Alpha emission</text>
</svg>"""
    create_or_update_svg_block(l141, 7, 'Nuclear Stability Belt, Neutron-to-Proton Ratio, and Spontaneous Decay Zones', 'nuclear_stability_belt_141', svg_141)
    print()

    # =========================================================================
    # LESSON 142: Types of Radioactivity
    # =========================================================================
    l142 = Lesson.objects.get(id=142)
    print(f'Enriching Lesson 142: \"{l142.title}\"')
    create_or_update_wm_block(
        l142, 2, 'Vintage Geiger-Müller Counter Tube Detecting Spontaneous Background Nuclear Radiation',
        'Geiger_counter_reading.jpg', 'Hannes Grobe', 'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Geiger_counter_reading.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l142, 3, 'High-Energy Particle Accelerator Target Chamber for Induced Artificial Nuclear Transmutation',
        'Particle_accelerator_chamber.jpg', 'CERN', 'CC BY 4.0',
        'https://commons.wikimedia.org/wiki/File:Particle_accelerator_chamber.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_142 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Taxonomy of Radioactivity: Natural Spontaneous vs. Induced Artificial</text>

  <!-- Left: Natural Radioactivity -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Natural Radioactivity (Spontaneous)</text>

  <rect x="60" y="115" width="330" height="135" fill="#0f172a" rx="8"/>
  <text x="225" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Spontaneous Disintegration of Heavy Nuclei</text>
  <text x="225" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">238_92U --&gt; 234_90Th + 4_2He (Alpha)</text>
  <text x="225" y="190" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">14_6C --&gt; 14_7N + 0_-1e (Beta)</text>
  <text x="225" y="215" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Occurs naturally in minerals (Uranium, Radium, Carbon-14)</text>
  <text x="225" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Unaffected by external Temperature, Pressure, or Catalyst</text>

  <rect x="60" y="265" width="330" height="140" fill="#0f172a" rx="6"/>
  <text x="225" y="290" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Discovery by Henri Becquerel (1896)</text>
  <text x="225" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Discovered uranium salts fogged wrapped photographic plates</text>
  <text x="225" y="338" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Marie &amp; Pierre Curie isolated Polonium and Radium</text>
  <text x="225" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Emits Alpha (α), Beta (β), and Gamma (γ) radiations</text>

  <!-- Right: Artificial Radioactivity -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Artificial Radioactivity (Induced)</text>

  <rect x="475" y="115" width="320" height="135" fill="#0f172a" rx="8"/>
  <text x="635" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Bombardment Transmutation of Stable Nuclei</text>
  <text x="635" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">14_7N + 4_2He --&gt; 17_8O + 1_1p (Rutherford, 1919)</text>
  <text x="635" y="190" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">27_13Al + 4_2He --&gt; 30_15P + 1_0n (Joliot-Curie, 1934)</text>
  <text x="635" y="215" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Stable target nucleus transformed by high-energy projectiles</text>
  <text x="635" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Projectiles: Neutrons, Protons, Alpha particles, Deuterons</text>

  <rect x="475" y="265" width="320" height="140" fill="#0f172a" rx="6"/>
  <text x="635" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Medical &amp; Industrial Radioisotopes</text>
  <text x="635" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cobalt-60 (60_27Co) for cancer radiation radiotherapy</text>
  <text x="635" y="338" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Iodine-131 (131_53I) for thyroid disorder diagnosis</text>
  <text x="635" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Americium-241 (241_95Am) for domestic smoke detectors</text>
</svg>"""
    create_or_update_svg_block(l142, 6, 'Natural Spontaneous Radioactivity vs Induced Artificial Nuclear Transmutation', 'types_radioactivity_142', svg_142)
    print()

    # =========================================================================
    # LESSON 143: Types of Radiation
    # =========================================================================
    l143 = Lesson.objects.get(id=143)
    print(f'Enriching Lesson 143: \"{l143.title}\"')
    create_or_update_wm_block(
        l143, 2, 'Cloud Chamber Particle Tracks Visualizing Distinct Alpha and Beta Radiation Trajectories',
        'Cloud_chamber_alpha_beta_tracks.jpg', 'Nuledo', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Cloud_chamber_alpha_beta_tracks.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l143, 3, 'Heavy Lead Castle Storage Container Designed to Shield High-Energy Gamma Radiation',
        'Lead_castle_radiation_shield.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Lead_castle_radiation_shield.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_143 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Sub-Atomic Architecture of the Three Nuclear Radiations (α, β, γ)</text>

  <!-- Alpha Particle -->
  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="245" height="355" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
    <text x="122" y="28" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Alpha Particle (α)</text>
    
    <rect x="15" y="45" width="215" height="110" fill="#0f172a" rx="8"/>
    <!-- 2 Protons + 2 Neutrons -->
    <circle cx="95" cy="85" r="14" fill="#ef4444"/><text x="95" y="89" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">p+</text>
    <circle cx="145" cy="85" r="14" fill="#ef4444"/><text x="145" y="89" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">p+</text>
    <circle cx="120" cy="115" r="14" fill="#64748b"/><text x="120" y="119" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">n0</text>
    <circle cx="120" cy="60" r="14" fill="#64748b"/><text x="120" y="64" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">n0</text>
    
    <rect x="15" y="165" width="215" height="175" fill="#0f172a" rx="6"/>
    <text x="122" y="190" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">4_2He (Helium Nucleus)</text>
    <text x="122" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mass: 4 atomic mass units (u)</text>
    <text x="122" y="235" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Charge: +2 (Two Protons)</text>
    <text x="122" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Velocity: ~5% - 10% speed of light</text>
    <text x="122" y="280" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Highest Ionizing Power</text>
    <text x="122" y="303" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Stopped by thin sheet of paper</text>
    <text x="122" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Range in air: 3 - 5 cm</text>
  </g>

  <!-- Beta Particle -->
  <g transform="translate(305, 65)">
    <rect x="0" y="0" width="245" height="355" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="122" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Beta Particle (β)</text>
    
    <rect x="15" y="45" width="215" height="110" fill="#0f172a" rx="8"/>
    <!-- Fast electron -->
    <circle cx="122" cy="100" r="16" fill="#38bdf8"/>
    <text x="122" y="105" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">e-</text>
    <text x="122" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">High-speed nuclear electron</text>
    
    <rect x="15" y="165" width="215" height="175" fill="#0f172a" rx="6"/>
    <text x="122" y="190" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">0_-1e (Fast Electron)</text>
    <text x="122" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mass: 1/1840 u (Negligible)</text>
    <text x="122" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Charge: -1 (One Electron)</text>
    <text x="122" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Velocity: Up to 90% speed of light</text>
    <text x="122" y="280" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Moderate Ionizing Power</text>
    <text x="122" y="303" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Stopped by 5 mm Aluminium sheet</text>
    <text x="122" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Range in air: ~1 meter</text>
  </g>

  <!-- Gamma Ray -->
  <g transform="translate(570, 65)">
    <rect x="0" y="0" width="250" height="355" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="125" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Gamma Ray (γ)</text>
    
    <rect x="15" y="45" width="220" height="110" fill="#0f172a" rx="8"/>
    <!-- High frequency EM wave -->
    <path d="M 30 100 Q 55 70 80 100 T 130 100 T 180 100 T 210 100" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <text x="125" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">High-energy photon wave (λ &lt; 10^-12 m)</text>
    
    <rect x="15" y="165" width="220" height="175" fill="#0f172a" rx="6"/>
    <text x="125" y="190" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">0_0γ (Electromagnetic Wave)</text>
    <text x="125" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mass: 0 (Pure photon energy)</text>
    <text x="125" y="235" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Charge: 0 (Neutral)</text>
    <text x="125" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Velocity: Speed of light (3 × 10^8 m/s)</text>
    <text x="125" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Lowest Ionizing Power</text>
    <text x="125" y="303" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Stopped only by thick Lead / Concrete</text>
    <text x="125" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Range in air: Hundreds of meters</text>
  </g>
</svg>"""
    create_or_update_svg_block(l143, 2, 'Sub-Atomic Architecture and Comparison Matrix of Alpha, Beta, and Gamma Radiations', 'types_radiations_matrix_143', svg_143)
    print()

    # =========================================================================
    # LESSON 144: Characteristics of Radiations
    # =========================================================================
    l144 = Lesson.objects.get(id=144)
    print(f'Enriching Lesson 144: \"{l144.title}\"')
    create_or_update_wm_block(
        l144, 2, 'Diffusion Cloud Chamber Operating Demonstration Showing Distinct Ionization Trails',
        'Cloud_chamber_tracks_display.jpg', 'Nuledo', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Cloud_chamber_tracks_display.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l144, 3, 'Scintillation Counter Crystal and Photomultiplier Detector for Measuring Radiation Energy',
        'Scintillation_counter_crystal.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Scintillation_counter_crystal.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_144 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Mechanical Analogy of Nuclear Radiations: Mass, Velocity &amp; Momentum</text>

  <!-- Left: Mechanical Bowling Ball Analogy -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Physical &amp; Mechanical Analogy</text>

  <rect x="60" y="115" width="330" height="85" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
  <text x="75" y="138" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Alpha (α) — "The Heavy Bowling Ball"</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Massive, slow, colossal momentum</text>
  <text x="75" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Plows into matter; knocks out electrons violently (Dense tracks)</text>

  <rect x="60" y="210" width="330" height="85" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
  <text x="75" y="233" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Beta (β) — "The Fast Ping-Pong Ball / Bullet"</text>
  <text x="75" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Extremely light, ultra high speed</text>
  <text x="75" y="275" fill="#fed7aa" font-family="system-ui, sans-serif" font-size="10">Zips through spaces between atoms; thin tortuous tracks</text>

  <rect x="60" y="305" width="330" height="85" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
  <text x="75" y="328" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Gamma (γ) — "The Pure Laser Beam"</text>
  <text x="75" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Massless, zero electric charge</text>
  <text x="75" y="370" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="10">Travels at light speed; passes straight through atomic lattices</text>

  <!-- Right: Quantitative Summary Table -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Quantitative Physical Properties</text>

  <g transform="translate(475, 115)">
    <rect x="0" y="0" width="320" height="60" fill="#0f172a" rx="6"/>
    <text x="15" y="25" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Kinetic Energy Distribution</text>
    <text x="15" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Alpha: Discrete monoenergetic (~5 MeV)</text>

    <rect x="0" y="70" width="320" height="60" fill="#0f172a" rx="6"/>
    <text x="15" y="95" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Beta Energy Spectrum</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Beta: Continuous spectrum (Shared with neutrino)</text>

    <rect x="0" y="140" width="320" height="60" fill="#0f172a" rx="6"/>
    <text x="15" y="165" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Velocity &amp; Relativistic Effects</text>
    <text x="15" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Beta reaches &gt;0.9c; exhibits relativistic mass gain</text>

    <rect x="0" y="210" width="320" height="70" fill="#0f172a" rx="6"/>
    <text x="160" y="235" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Cloud Chamber Appearance</text>
    <text x="160" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">α: Broad straight dense lines | β: Faint crooked lines</text>
  </g>
</svg>"""
    create_or_update_svg_block(l144, 2, 'Physical Characteristics and Mechanical Momentum Analogy of Alpha, Beta, and Gamma Radiations', 'radiation_characteristics_144', svg_144)
    print()

    # =========================================================================
    # LESSON 145: Properties of Radiations
    # =========================================================================
    l145 = Lesson.objects.get(id=145)
    print(f'Enriching Lesson 145: \"{l145.title}\"')
    create_or_update_wm_block(
        l145, 2, 'Gold Leaf Electroscope Discharging Rapidly When Ionizing Alpha Radiation is Brought Near',
        'Gold_leaf_electroscope_discharge.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Gold_leaf_electroscope_discharge.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l145, 3, 'Fluorescent Zinc Sulfide Scintillator Screen Glowing Green Under Alpha Particle Bombardment',
        'Zinc_sulfide_scintillation.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Zinc_sulfide_scintillation.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_145 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Fundamental Law of Inverse Properties: Ionizing Power vs. Penetrating Ability</text>

  <!-- Inverse Trade-off Diagram -->
  <rect x="40" y="65" width="780" height="355" fill="#1e293b" rx="12" stroke="#64748b" stroke-width="2"/>
  
  <!-- Row 1 Alpha -->
  <rect x="60" y="90" width="740" height="95" fill="#0f172a" rx="8" stroke="#f87171" stroke-width="1"/>
  <text x="80" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Alpha Particles (α): Maximum Ionization / Minimum Penetration</text>
  <text x="80" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Relative Ionizing Strength: <tspan fill="#facc15" font-weight="bold">10,000</tspan> (Creates 100,000 ion pairs per cm in air)</text>
  <text x="80" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Penetrating Power: <tspan fill="#f87171" font-weight="bold">1</tspan> (Stopped by thin paper or dead outer skin layer)</text>
  <text x="80" y="178" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Reason: Large +2 charge and slow velocity cause frequent energy-draining collisions with air atoms.</text>

  <!-- Row 2 Beta -->
  <rect x="60" y="195" width="740" height="95" fill="#0f172a" rx="8" stroke="#fbbf24" stroke-width="1"/>
  <text x="80" y="220" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Beta Particles (β): Moderate Ionization / Moderate Penetration</text>
  <text x="80" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Relative Ionizing Strength: <tspan fill="#facc15" font-weight="bold">100</tspan> (Creates ~1,000 ion pairs per cm in air)</text>
  <text x="80" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Penetrating Power: <tspan fill="#fbbf24" font-weight="bold">100</tspan> (Stopped by 5 mm Aluminium or perspex sheet)</text>
  <text x="80" y="283" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Reason: -1 charge and higher velocity cause fewer collisions, penetrating deeper before exhausting kinetic energy.</text>

  <!-- Row 3 Gamma -->
  <rect x="60" y="300" width="740" height="105" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
  <text x="80" y="325" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Gamma Rays (γ): Minimum Ionization / Maximum Penetration</text>
  <text x="80" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Relative Ionizing Strength: <tspan fill="#facc15" font-weight="bold">1</tspan> (Rare direct photoelectric/Compton interactions)</text>
  <text x="80" y="370" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Penetrating Power: <tspan fill="#4ade80" font-weight="bold">10,000</tspan> (Requires thick Lead / high-density Concrete to attenuate)</text>
  <text x="80" y="393" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Golden Rule: A radiation cannot possess both extreme penetrating power and extreme ionizing power simultaneously!</text>
</svg>"""
    create_or_update_svg_block(l145, 2, 'The Inverse Law of Nuclear Radiation: Relative Ionizing Power vs Penetrating Distance', 'radiation_inverse_law_145', svg_145)
    print()

    # =========================================================================
    # LESSON 146: Penetrating Power
    # =========================================================================
    l146 = Lesson.objects.get(id=146)
    print(f'Enriching Lesson 146: \"{l146.title}\"')
    create_or_update_wm_block(
        l146, 2, 'Demonstration of Radiation Penetration Through Thin Paper Sheet and Aluminium Foil',
        'Radiation_penetration_experiment.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Radiation_penetration_experiment.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l146, 3, 'High-Density Lead Shielding Bricks Used in Nuclear Radiochemistry Laboratories',
        'Lead_bricks_radiation_shielding.jpg', 'US Department of Energy', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Lead_bricks_radiation_shielding.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_146 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Comparative Penetrating Power of Alpha, Beta, and Gamma Radiations</text>

  <!-- Radiation Source -->
  <rect x="40" y="110" width="70" height="260" fill="#1e293b" rx="8" stroke="#facc15" stroke-width="2"/>
  <text x="75" y="240" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 75,240)">RADIOACTIVE SOURCE</text>

  <!-- Barriers -->
  <!-- 1. Paper -->
  <rect x="230" y="90" width="12" height="300" fill="#e2e8f0" rx="2"/>
  <text x="236" y="75" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Paper (0.1 mm)</text>

  <!-- 2. Aluminium -->
  <rect x="440" y="90" width="24" height="300" fill="#94a3b8" rx="2"/>
  <text x="452" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Aluminium (5 mm)</text>

  <!-- 3. Lead / Concrete -->
  <rect x="670" y="90" width="60" height="300" fill="#475569" rx="4"/>
  <text x="700" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Lead (10 cm)</text>

  <!-- Radiation Beams -->
  <!-- Alpha Beam (stops at paper) -->
  <line x1="110" y1="150" x2="230" y2="150" stroke="#f87171" stroke-width="6"/>
  <text x="170" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Alpha (α)</text>
  <circle cx="230" cy="150" r="8" fill="#ef4444"/>
  <text x="290" y="155" fill="#f87171" font-size="11" font-weight="bold">STOPPED</text>

  <!-- Beta Beam (passes paper, stops at Al) -->
  <line x1="110" y1="240" x2="440" y2="240" stroke="#fbbf24" stroke-width="4"/>
  <text x="170" y="230" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Beta (β)</text>
  <circle cx="440" cy="240" r="8" fill="#f59e0b"/>
  <text x="500" y="245" fill="#fbbf24" font-size="11" font-weight="bold">STOPPED</text>

  <!-- Gamma Beam (passes paper, Al, and attenuated by lead) -->
  <path d="M 110 330 Q 130 315 150 330 T 190 330 T 230 330 T 270 330 T 310 330 T 350 330 T 390 330 T 430 330 T 470 330 T 510 330 T 550 330 T 590 330 T 630 330 T 670 330" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <text x="170" y="320" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Gamma (γ)</text>
  <!-- Thin attenuated line after lead -->
  <line x1="730" y1="330" x2="820" y2="330" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3"/>
  <text x="775" y="320" fill="#38bdf8" font-size="11">Attenuated</text>

  <!-- Footer summary -->
  <rect x="40" y="405" width="780" height="35" fill="#1e293b" rx="6"/>
  <text x="430" y="428" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Penetration Hierarchy: <tspan fill="#f87171" font-weight="bold">Alpha (Paper)</tspan> &lt; <tspan fill="#fbbf24" font-weight="bold">Beta (Aluminium)</tspan> &lt; <tspan fill="#38bdf8" font-weight="bold">Gamma (Dense Lead / Concrete)</tspan></text>
</svg>"""
    create_or_update_svg_block(l146, 2, 'Penetrating Power and Shielding Barrier Demonstration: Paper, Aluminium, and Lead', 'penetrating_power_barriers_146', svg_146)
    print()

    # =========================================================================
    # LESSON 147: Deflection by an Electric/Magnetic Field
    # =========================================================================
    l147 = Lesson.objects.get(id=147)
    print(f'Enriching Lesson 147: \"{l147.title}\"')
    create_or_update_wm_block(
        l147, 2, 'Cathode Ray Deflection Tube Demonstrating Electric and Magnetic Field Curvature',
        'Cathode_ray_deflection_tube.jpg', 'D-Kuru', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Cathode_ray_deflection_tube.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l147, 4, 'Electromagnet Pole Pieces Creating Uniform Magnetic Field for Particle Separation',
        'Electromagnet_magnetic_field_poles.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Electromagnet_magnetic_field_poles.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_147 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Deflection of Nuclear Radiations in Electric and Magnetic Fields</text>

  <!-- Left: Electric Field Chamber -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Behavior in an Electric Field</text>

  <!-- Positive Plate Top -->
  <rect x="120" y="115" width="220" height="20" fill="#ef4444" rx="3"/>
  <text x="230" y="130" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">POSITIVE PLATE (+)</text>

  <!-- Negative Plate Bottom -->
  <rect x="120" y="275" width="220" height="20" fill="#38bdf8" rx="3"/>
  <text x="230" y="290" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">NEGATIVE PLATE (-)</text>

  <!-- Lead Collimator Source -->
  <rect x="60" y="180" width="40" height="50" fill="#475569" rx="4"/>
  <circle cx="80" cy="205" r="5" fill="#facc15"/>

  <!-- Beams -->
  <!-- Beta: Large upward curvature towards positive plate -->
  <path d="M 100 205 Q 180 205 320 145" stroke="#fbbf24" stroke-width="3" fill="none"/>
  <text x="360" y="148" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">β (Large deflection to +)</text>

  <!-- Gamma: Undeviated straight line -->
  <line x1="100" y1="205" x2="380" y2="205" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>
  <text x="360" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">γ (Undeviated)</text>

  <!-- Alpha: Small downward curvature towards negative plate -->
  <path d="M 100 205 Q 200 205 320 260" stroke="#f87171" stroke-width="4" fill="none"/>
  <text x="360" y="265" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">α (Slight deflection to -)</text>

  <rect x="60" y="315" width="330" height="90" fill="#0f172a" rx="6"/>
  <text x="225" y="338" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Why Beta Deflects More Than Alpha</text>
  <text x="225" y="358" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Deflection ∝ Charge / Mass ratio (q/m)</text>
  <text x="225" y="378" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Beta electron is ~7360x lighter than Alpha particle</text>
  <text x="225" y="398" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Gamma has zero charge (q=0) --&gt; no deflection</text>

  <!-- Right: Magnetic Field Deflection -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Behavior in a Magnetic Field</text>

  <!-- Fleming's Left-Hand Rule Box -->
  <rect x="475" y="115" width="320" height="180" fill="#0f172a" rx="8"/>
  <text x="635" y="140" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Fleming's Left-Hand Rule Direction</text>
  
  <text x="635" y="170" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Alpha (Positive Current into page):</text>
  <text x="635" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Deflected in one direction (e.g. Upwards)</text>

  <text x="635" y="225" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Beta (Negative Charge = Opposite Current):</text>
  <text x="635" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Deflected in exact opposite direction (e.g. Downwards)</text>

  <text x="635" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Gamma (Photons): Zero deflection (Straight path)</text>

  <rect x="475" y="315" width="320" height="90" fill="#0f172a" rx="6"/>
  <text x="635" y="338" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Experimental Verification</text>
  <text x="635" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Proves that α and β particles carry opposite electric charges</text>
  <text x="635" y="385" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">and confirms the neutral photon nature of γ radiation</text>
</svg>"""
    create_or_update_svg_block(l147, 3, 'Electric and Magnetic Field Deflection Chambers for Alpha, Beta, and Gamma Rays', 'field_deflection_chambers_147', svg_147)
    print()

    # =========================================================================
    # LESSON 148: Ionising Effect of Radiations
    # =========================================================================
    l148 = Lesson.objects.get(id=148)
    print(f'Enriching Lesson 148: \"{l148.title}\"')
    create_or_update_wm_block(
        l148, 2, 'Ionization Chamber Detector Demonstrating Current Flow from Radiation-Induced Ion Pairs',
        'Ionization_chamber_cutaway.jpg', 'US NRC', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Ionization_chamber_cutaway.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l148, 4, 'Domestic Ionization Smoke Detector Mechanism Powered by Americium-241 Alpha Source',
        'Smoke_detector_americium_chamber.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Smoke_detector_americium_chamber.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_148 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Ionising Effect of Nuclear Radiations: Mechanism &amp; Smoke Detector Application</text>

  <!-- Left: Sub-Microscopic Ionization -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="225" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Sub-Microscopic Ion Pair Creation</text>

  <g transform="translate(65, 115)">
    <rect x="0" y="0" width="320" height="140" fill="#0f172a" rx="8"/>
    <!-- Alpha particle plowing through -->
    <circle cx="50" cy="70" r="16" fill="#ef4444"/>
    <text x="50" y="74" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">α (2+)</text>

    <!-- Neutral Gas Atom knocked -->
    <circle cx="160" cy="70" r="22" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <text x="160" y="74" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">N2 / O2</text>

    <!-- Knocked out electron -->
    <path d="M 175 60 L 250 30" stroke="#facc15" stroke-width="2" stroke-dasharray="2"/>
    <circle cx="255" cy="28" r="6" fill="#facc15"/><text x="255" y="31" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">e-</text>
    <text x="285" y="32" fill="#facc15" font-size="10" font-weight="bold">Free Electron</text>

    <!-- Positive Ion created -->
    <path d="M 175 80 L 250 110" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2"/>
    <circle cx="255" cy="112" r="10" fill="#38bdf8"/><text x="255" y="116" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">+</text>
    <text x="290" y="115" fill="#38bdf8" font-size="10" font-weight="bold">Positive Ion (N2+)</text>
  </g>

  <rect x="60" y="270" width="330" height="135" fill="#0f172a" rx="6"/>
  <text x="225" y="295" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Kinetic Energy Transfer (Linear Energy Transfer)</text>
  <text x="225" y="318" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Alpha particle exerts strong electrostatic attraction on electrons</text>
  <text x="225" y="340" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Rips valence electrons free, creating an <tspan fill="#facc15" font-weight="bold">Ion Pair</tspan></text>
  <text x="225" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Alpha creates ~100,000 ion pairs per cm before stopping</text>
  <text x="225" y="390" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Severe biological DNA damage if alpha emitter is inhaled</text>

  <!-- Right: Smoke Detector -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Domestic Smoke Detector Application</text>

  <rect x="475" y="115" width="320" height="140" fill="#0f172a" rx="8"/>
  <text x="635" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Americium-241 Ionization Chamber</text>
  <text x="635" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">1. Tiny Am-241 source continuously ionizes air in chamber</text>
  <text x="635" y="185" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2. Ions drift to electrodes, creating steady tiny electric current</text>
  <text x="635" y="210" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">3. Smoke particles enter --&gt; attach to ions --&gt; Current DROPS</text>
  <text x="635" y="235" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">4. Microchip detects current drop and sounds loud ALARM</text>

  <rect x="475" y="270" width="320" height="135" fill="#0f172a" rx="6"/>
  <text x="635" y="295" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Why Alpha Source is Safe in Smoke Detectors</text>
  <text x="635" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Alpha particles cannot penetrate plastic detector casing</text>
  <text x="635" y="342" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Zero external radiation hazard to room occupants</text>
  <text x="635" y="368" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Am-241 half-life = 432 years (Requires no maintenance)</text>
</svg>"""
    create_or_update_svg_block(l148, 3, 'Sub-Microscopic Air Ionization Mechanism and Smoke Detector Circuit Operation', 'ionization_smoke_detector_148', svg_148)
    print()

    # =========================================================================
    # LESSON 149: Radioactive Decay and Half-Life
    # =========================================================================
    l149 = Lesson.objects.get(id=149)
    print(f'Enriching Lesson 149: \"{l149.title}\"')
    create_or_update_wm_block(
        l149, 2, 'Decay Counting Experiment Setup Measuring Radioactive Sample Activity Over Time',
        'Radioactive_decay_counter_lab.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Radioactive_decay_counter_lab.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l149, 5, 'Radiocarbon Accelerator Mass Spectrometry Laboratory for Archaeological Sample Dating',
        'Radiocarbon_dating_ams_lab.jpg', 'Rama', 'CeCILL',
        'https://commons.wikimedia.org/wiki/File:Radiocarbon_dating_ams_lab.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_149 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Radioactive Decay &amp; Half-Life: Exponential Decay Curve &amp; Calculation Formula</text>

  <!-- Left: Half Life Curve -->
  <rect x="40" y="65" width="440" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="260" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Exponential Decay Curve: Iodine-131 (t1/2 = 8 Days)</text>

  <g transform="translate(65, 115)">
    <!-- Axes -->
    <line x1="40" y1="230" x2="380" y2="230" stroke="#94a3b8" stroke-width="2"/>
    <line x1="40" y1="230" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
    <text x="210" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Time Elapsed (Days / Half-Lives)</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle" transform="rotate(-90 15,125)">Remaining Mass (g / %)</text>

    <!-- Grid points -->
    <!-- (0, 100g) -> (8d, 50g) -> (16d, 25g) -> (24d, 12.5g) -> (32d, 6.25g) -->
    <!-- x scale: 0d=40, 8d=110, 16d=180, 24d=250, 32d=320 -->
    <!-- y scale: 100g=30, 50g=130, 25g=180, 12.5g=205, 6.25g=218 -->
    <path d="M 40 30 Q 110 130 180 180 T 250 205 T 320 218 T 370 225" stroke="#38bdf8" stroke-width="4" fill="none"/>

    <circle cx="40" cy="30" r="5" fill="#facc15"/><text x="40" y="20" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">100g (N0)</text>
    <circle cx="110" cy="130" r="5" fill="#facc15"/><text x="110" y="120" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">50g (1 t1/2)</text>
    <circle cx="180" cy="180" r="5" fill="#facc15"/><text x="180" y="170" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">25g (2 t1/2)</text>
    <circle cx="250" cy="205" r="5" fill="#facc15"/><text x="250" y="195" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">12.5g (3 t1/2)</text>
    <circle cx="320" cy="218" r="5" fill="#facc15"/><text x="320" y="210" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">6.25g (4 t1/2)</text>

    <!-- Drop lines for t1/2 = 8 days -->
    <line x1="110" y1="130" x2="110" y2="230" stroke="#facc15" stroke-dasharray="2"/>
    <text x="110" y="242" fill="#facc15" font-size="9" text-anchor="middle">8d</text>
    <line x1="180" y1="180" x2="180" y2="230" stroke="#facc15" stroke-dasharray="2"/>
    <text x="180" y="242" fill="#facc15" font-size="9" text-anchor="middle">16d</text>
    <line x1="250" y1="205" x2="250" y2="230" stroke="#facc15" stroke-dasharray="2"/>
    <text x="250" y="242" fill="#facc15" font-size="9" text-anchor="middle">24d</text>
    <line x1="320" y1="218" x2="320" y2="230" stroke="#facc15" stroke-dasharray="2"/>
    <text x="320" y="242" fill="#facc15" font-size="9" text-anchor="middle">32d</text>
  </g>

  <!-- Right: Mathematical Formula & Worked Rules -->
  <rect x="500" y="65" width="320" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="660" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Mathematical Half-Life Formula</text>

  <rect x="520" y="115" width="280" height="95" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
  <text x="660" y="145" fill="#38bdf8" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">N(t) = N0 × (1/2)^n</text>
  <text x="660" y="170" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Where n = t / t1/2 (Number of Half-Lives)</text>
  <text x="660" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">N0 = Initial mass/activity | N(t) = Remaining mass</text>

  <rect x="520" y="220" width="280" height="195" fill="#0f172a" rx="6"/>
  <text x="660" y="245" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Standard Fraction Step Method</text>
  
  <text x="535" y="270" fill="#cbd5e1" font-family="monospace" font-size="11">• n = 1: Remaining = 1/2 (50%)</text>
  <text x="535" y="295" fill="#cbd5e1" font-family="monospace" font-size="11">• n = 2: Remaining = 1/4 (25%)</text>
  <text x="535" y="320" fill="#cbd5e1" font-family="monospace" font-size="11">• n = 3: Remaining = 1/8 (12.5%)</text>
  <text x="535" y="345" fill="#cbd5e1" font-family="monospace" font-size="11">• n = 4: Remaining = 1/16 (6.25%)</text>
  <text x="535" y="370" fill="#cbd5e1" font-family="monospace" font-size="11">• n = 5: Remaining = 1/32 (3.125%)</text>
  <text x="660" y="398" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Half-life is constant and independent of sample size</text>
</svg>"""
    create_or_update_svg_block(l149, 4, 'Radioactive Decay Exponential Half-Life Curve, Fractional Reduction, and Formula Roadmap', 'halflife_decay_curve_149', svg_149)
    print()

    print('=== First Half of Topic 7 (Lessons 141 - 149) Completed Successfully! ===')

if __name__ == '__main__':
    enrich_topic7_first_half()
