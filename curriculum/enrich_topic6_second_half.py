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
    
    # We look for a block that either is on page_num without an AI asset or create new
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

def enrich_topic6_second_half():
    print('=== ENRICHING FORM 4 TOPIC 6: ORGANIC CHEMISTRY II (SECOND HALF: LESSONS 129 - 140) ===\n')

    # =========================================================================
    # LESSON 129: Detergents — Introduction
    # =========================================================================
    l129 = Lesson.objects.get(id=129)
    print(f'Enriching Lesson 129: \"{l129.title}\"')
    create_or_update_wm_block(
        l129, 2, 'Assorted Commercial Toilet Soaps and Modern Synthetic Detergent Powders',
        'Soaps_and_detergent_bars.jpg', 'Evan-Amos', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Soaps_and_detergent_bars.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l129, 3, 'Surface Tension Demonstration: Water Droplet Forming a Spherical Bead on a Waxy Hydrophobic Leaf',
        'Water_droplet_on_lotus_leaf.jpg', 'Shin-G', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Water_droplet_on_lotus_leaf.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_129 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Classification of Detergents: Soapy vs. Soapless Cleaning Agents</text>

  <!-- Left: Soapy Detergents -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Soapy Detergents (Soaps)</text>

  <rect x="60" y="115" width="330" height="135" fill="#0f172a" rx="8"/>
  <text x="225" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Sodium / Potassium Salts of Fatty Acids</text>
  <text x="225" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">R — COO- Na+ (e.g. C17H35COONa)</text>
  <text x="225" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Made from natural animal fats or plant vegetable oils</text>
  <text x="225" y="210" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• 100% Biodegradable (environmentally benign)</text>
  <text x="225" y="230" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Forms insoluble SCUM in hard water (wastes soap)</text>

  <rect x="60" y="265" width="330" height="140" fill="#0f172a" rx="6"/>
  <text x="225" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Surfactant Surface Tension Lowering</text>
  <text x="225" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Concentrates at the water-air interface</text>
  <text x="225" y="338" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Breaks hydrogen bonding network of water surface</text>
  <text x="225" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Allows water to penetrate and wet fabric fibers</text>
  <text x="225" y="385" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Enables detachment of greasy dirt particles</text>

  <!-- Right: Soapless Detergents -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Soapless Detergents (Synthetic)</text>

  <rect x="475" y="115" width="320" height="135" fill="#0f172a" rx="8"/>
  <text x="635" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Sodium Alkylbenzene Sulfonates / Sulfates</text>
  <text x="635" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">R — C6H4 — SO3- Na+  or  R — OSO3- Na+</text>
  <text x="635" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Synthesized from petrochemical crude oil fractions</text>
  <text x="635" y="210" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Works perfectly in HARD water (No Scum!)</text>
  <text x="635" y="230" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Calcium/Magnesium sulfonates remain soluble</text>

  <rect x="475" y="265" width="320" height="140" fill="#0f172a" rx="6"/>
  <text x="635" y="290" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Environmental Distinction</text>
  <text x="635" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Branched-chain detergents resist bacteria (Pollution)</text>
  <text x="635" y="338" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Modern straight-chain LAS are readily biodegradable</text>
  <text x="635" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• May contain phosphate builders that cause eutrophication</text>
  <text x="635" y="385" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Superior cleaning power in cold / acidic water</text>
</svg>"""
    create_or_update_svg_block(l129, 4, 'Classification Hierarchy and Comparative Chemistry of Soapy and Soapless Detergents', 'detergent_classification_129', svg_129)
    print()

    # =========================================================================
    # LESSON 130: Soapy Detergents
    # =========================================================================
    l130 = Lesson.objects.get(id=130)
    print(f'Enriching Lesson 130: \"{l130.title}\"')
    create_or_update_wm_block(
        l130, 2, 'Traditional Cold-Process Soap Bar Curing and Saponification Mixture',
        'Handmade_soap_bars_curing.jpg', 'Fir0002', 'GFDL 1.2',
        'https://commons.wikimedia.org/wiki/File:Handmade_soap_bars_curing.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l130, 3, 'Glycerol (Propane-1,2,3-triol) Pure Chemical Reagent Liquid Byproduct of Saponification',
        'Glycerol_reagent_bottle.jpg', 'LHcheM', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Glycerol_reagent_bottle.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_130 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Saponification: Alkaline Hydrolysis of Triglycerides &amp; Salting Out of Soap</text>

  <!-- Left: Saponification Reaction -->
  <rect x="40" y="65" width="460" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="270" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Saponification Chemistry (Alkaline Hydrolysis)</text>

  <rect x="60" y="115" width="420" height="150" fill="#0f172a" rx="8"/>
  <text x="270" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Triglyceride Fat (Glyceryl Stearate) + Sodium Hydroxide</text>
  <text x="270" y="170" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">(C17H35COO)3C3H5 + 3NaOH(aq) --[Boil]--&gt;</text>
  <text x="270" y="200" fill="#4ade80" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">3C17H35COONa(s) + C3H5(OH)3(aq)</text>
  <text x="270" y="230" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">[Sodium Stearate Soap]  +  [Glycerol / Propane-1,2,3-triol]</text>

  <rect x="60" y="280" width="420" height="135" fill="#0f172a" rx="6"/>
  <text x="270" y="305" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">The Role of Concentrated Brine (Salting Out)</text>
  <text x="270" y="328" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Saturated NaCl solution added to precipitate soap curd</text>
  <text x="270" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• High Na+ concentration shifts ionic equilibrium (Common Ion Effect)</text>
  <text x="270" y="372" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Solid soap floats on dense brine lye and is skimmed off</text>
  <text x="270" y="395" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Glycerol in bottom aqueous layer recovered for cosmetics</text>

  <!-- Right: Anatomy of Soap Molecule -->
  <rect x="520" y="65" width="300" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="670" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Anatomy of a Soap Molecule</text>

  <!-- Tail & Head -->
  <rect x="540" y="120" width="260" height="130" fill="#0f172a" rx="8"/>
  <text x="670" y="145" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Hydrophobic Non-Polar Tail</text>
  <path d="M 560 175 L 575 165 L 590 175 L 605 165 L 620 175 L 635 165 L 650 175 L 665 165 L 680 175" stroke="#facc15" stroke-width="3" fill="none"/>
  <text x="620" y="200" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">C17H35— (Alkyl Chain)</text>
  <text x="620" y="225" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Oil-soluble / Water-repelling</text>

  <circle cx="735" cy="170" r="22" fill="#38bdf8"/>
  <text x="735" y="174" fill="#0f172a" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" text-anchor="middle">-COO-</text>
  <text x="735" y="210" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Ionic Head</text>
  <text x="735" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Water-soluble</text>

  <rect x="540" y="265" width="260" height="150" fill="#0f172a" rx="6"/>
  <text x="670" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Hard vs Soft Soaps</text>
  <text x="670" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• NaOH produces solid Hard Soap</text>
  <text x="670" y="338" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">(Laundry bars, bar soaps)</text>
  <text x="670" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• KOH produces Soft / Liquid Soap</text>
  <text x="670" y="388" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">(Shaving cream, shampoo)</text>
</svg>"""
    create_or_update_svg_block(l130, 4, 'Saponification Alkaline Hydrolysis Mechanism, Salting Out, and Soap Molecular Structure', 'saponification_mechanism_130', svg_130)
    print()

    # =========================================================================
    # LESSON 131: The Mode of Action of Soap in Cleaning
    # =========================================================================
    l131 = Lesson.objects.get(id=131)
    print(f'Enriching Lesson 131: \"{l131.title}\"')
    create_or_update_wm_block(
        l131, 2, 'Dense White Foam Lather Formed by Soap Agitation in Soft Water',
        'Soap_foam_bubbles.jpg', 'Nevit Dilmen', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Soap_foam_bubbles.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l131, 3, 'Oil and Water Emulsion Droplets Stabilized in Aqueous Soap Solution',
        'Oil_in_water_emulsion.jpg', 'Fvasconcellos', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Oil_in_water_emulsion.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_131 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Step-by-Step Micelle Emulsification Mechanism of Soap in Washing</text>

  <!-- Step 1 Wetting -->
  <rect x="40" y="65" width="245" height="365" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
  <text x="162" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Step 1: Wetting &amp; Penetration</text>
  <rect x="55" y="115" width="215" height="150" fill="#0f172a" rx="6"/>
  <!-- Fabric with grease -->
  <rect x="70" y="210" width="185" height="25" fill="#475569" rx="2"/>
  <text x="162" y="227" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Cloth Fabric Fibres</text>
  <ellipse cx="162" cy="195" rx="40" ry="15" fill="#fbbf24"/>
  <text x="162" y="198" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Grease / Oil</text>
  <!-- Tails pointing in -->
  <line x1="140" y1="150" x2="150" y2="185" stroke="#facc15" stroke-width="2"/>
  <circle cx="140" cy="150" r="5" fill="#38bdf8"/>
  <line x1="185" y1="150" x2="175" y2="185" stroke="#facc15" stroke-width="2"/>
  <circle cx="185" cy="150" r="5" fill="#38bdf8"/>

  <rect x="55" y="275" width="215" height="140" fill="#0f172a" rx="6"/>
  <text x="162" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Hydrophobic tails dissolve in grease</text>
  <text x="162" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Hydrophilic heads remain in water</text>
  <text x="162" y="350" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Lowers interfacial tension</text>
  <text x="162" y="380" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Water penetrates fabric pores</text>

  <!-- Step 2 Agitation & Detachment -->
  <rect x="305" y="65" width="245" height="365" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
  <text x="427" y="95" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Step 2: Mechanical Lift-Off</text>
  <rect x="320" y="115" width="215" height="150" fill="#0f172a" rx="6"/>
  <!-- Grease lifted -->
  <rect x="335" y="235" width="185" height="20" fill="#475569" rx="2"/>
  <circle cx="427" cy="170" r="30" fill="#fbbf24"/>
  <text x="427" y="174" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Oil Droplet</text>
  <!-- Tails radially inserted -->
  <circle cx="427" cy="130" r="5" fill="#38bdf8"/><line x1="427" y1="135" x2="427" y2="150" stroke="#facc15" stroke-width="2"/>
  <circle cx="427" cy="210" r="5" fill="#38bdf8"/><line x1="427" y1="205" x2="427" y2="190" stroke="#facc15" stroke-width="2"/>
  <circle cx="387" cy="170" r="5" fill="#38bdf8"/><line x1="392" y1="170" x2="407" y2="170" stroke="#facc15" stroke-width="2"/>
  <circle cx="467" cy="170" r="5" fill="#38bdf8"/><line x1="462" y1="170" x2="447" y2="170" stroke="#facc15" stroke-width="2"/>

  <rect x="320" y="275" width="215" height="140" fill="#0f172a" rx="6"/>
  <text x="427" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Agitation pulls grease from cloth</text>
  <text x="427" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Grease breaks into micro-globules</text>
  <text x="427" y="350" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Spherical micelle formation begins</text>
  <text x="427" y="380" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Cloth surface left clean</text>

  <!-- Step 3 Emulsion & Suspension -->
  <rect x="570" y="65" width="250" height="365" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
  <text x="695" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Step 3: Stable Emulsion</text>
  <rect x="585" y="115" width="220" height="150" fill="#0f172a" rx="6"/>
  <!-- Micelles suspended -->
  <circle cx="695" cy="170" r="32" fill="#fbbf24"/>
  <text x="695" y="174" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">OIL CORE</text>
  <!-- Full ring of heads -->
  <circle cx="695" cy="128" r="5" fill="#38bdf8"/><circle cx="695" cy="212" r="5" fill="#38bdf8"/>
  <circle cx="653" cy="170" r="5" fill="#38bdf8"/><circle cx="737" cy="170" r="5" fill="#38bdf8"/>
  <circle cx="665" cy="140" r="5" fill="#38bdf8"/><circle cx="725" cy="140" r="5" fill="#38bdf8"/>
  <circle cx="665" cy="200" r="5" fill="#38bdf8"/><circle cx="725" cy="200" r="5" fill="#38bdf8"/>

  <rect x="585" y="275" width="220" height="140" fill="#0f172a" rx="6"/>
  <text x="695" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Outer -COO- heads form negative shell</text>
  <text x="695" y="325" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Micelles mutually repel (No coalescence)</text>
  <text x="695" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Stable colloidal emulsion rinsed away</text>
  <text x="695" y="380" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Complete removal of grease in rinse</text>
</svg>"""
    create_or_update_svg_block(l131, 4, 'Sub-Microscopic Soap Micelle Emulsification and Cleaning Mechanism in Washing', 'soap_cleaning_mechanism_131', svg_131)
    print()

    # =========================================================================
    # LESSON 132: Effect of Hard Water on Soap
    # =========================================================================
    l132 = Lesson.objects.get(id=132)
    print(f'Enriching Lesson 132: \"{l132.title}\"')
    create_or_update_wm_block(
        l132, 2, 'Curdy White Insoluble Scum Precipitate Formed by Soap in Hard Water Containing Calcium and Magnesium Ions',
        'Soap_scum_in_water.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Soap_scum_in_water.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l132, 3, 'Boiler Scale and Mineral Crust Encrustations Inside Domestic Electric Kettle Heating Element',
        'Limescale_on_heating_element.jpg', 'Santeri Viinamäki', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Limescale_on_heating_element.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_132 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Hard Water Interaction with Soap: The Chemistry of Scum Formation</text>

  <!-- Left: Scum Formation Chemistry -->
  <rect x="40" y="65" width="460" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="270" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Precipitation of Insoluble Stearates (Scum)</text>

  <rect x="60" y="115" width="420" height="140" fill="#0f172a" rx="8"/>
  <text x="270" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Reaction with Dissolved Calcium &amp; Magnesium Ions</text>
  <text x="270" y="168" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">2C17H35COONa(aq) + Ca2+(aq) --&gt; (C17H35COO)2Ca(s) + 2Na+(aq)</text>
  <text x="270" y="193" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">2C17H35COONa(aq) + Mg2+(aq) --&gt; (C17H35COO)2Mg(s) + 2Na+(aq)</text>
  <text x="270" y="220" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Calcium Stearate / Magnesium Stearate (Insoluble Grey-White Scum)</text>

  <rect x="60" y="270" width="420" height="135" fill="#0f172a" rx="6"/>
  <text x="270" y="295" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Why Hard Water Wastes Large Quantities of Soap</text>
  <text x="270" y="318" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• No lather can form until ALL Ca2+ and Mg2+ ions are precipitated</text>
  <text x="270" y="340" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Huge waste of expensive soap before cleansing begins</text>
  <text x="270" y="365" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Sticky scum adheres to white fabrics, causing greying &amp; stiffness</text>
  <text x="270" y="388" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Forms dirty scum rings on baths and washing basins</text>

  <!-- Right: Comparison Soft vs Hard -->
  <rect x="520" y="65" width="300" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="670" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Soft vs Hard Water</text>

  <rect x="540" y="115" width="260" height="130" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
  <text x="670" y="138" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Soft Water (Rainwater)</text>
  <text x="670" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Zero Ca2+ or Mg2+ ions</text>
  <text x="670" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Instant rich lather with minimal soap</text>
  <text x="670" y="200" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• 100% efficient washing</text>

  <rect x="540" y="260" width="260" height="145" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
  <text x="670" y="285" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Hard Water (Mineral Springs)</text>
  <text x="670" y="308" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• High Ca(HCO3)2, CaSO4, MgSO4</text>
  <text x="670" y="330" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Heavy scum precipitation</text>
  <text x="670" y="352" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Solved by using soapless detergents</text>
  <text x="670" y="375" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">or softening with Na2CO3 / Zeolite</text>
</svg>"""
    create_or_update_svg_block(l132, 4, 'Hard Water Scum Formation Chemistry and Comparative Soft Water Washing Efficiency', 'hard_water_soap_scum_132', svg_132)
    print()

    # =========================================================================
    # LESSON 133: Soapless Detergents (Synthetic Detergents)
    # =========================================================================
    l133 = Lesson.objects.get(id=133)
    print(f'Enriching Lesson 133: \"{l133.title}\"')
    create_or_update_wm_block(
        l133, 2, 'Commercial Synthetic Liquid Dishwashing Detergent and Sulfonate Washing Powder',
        'Dishwashing_liquid_detergent.jpg', 'Evan-Amos', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Dishwashing_liquid_detergent.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l133, 4, 'Laboratory Alkylbenzene Sulfonation Preparation Setup with Concentrated Sulfuric Acid',
        'Sulfonation_lab_reaction.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Sulfonation_lab_reaction.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_133 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Synthetic Soapless Detergents: Molecular Architecture &amp; Hard Water Resilience</text>

  <!-- Left: Molecular Structure -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Sodium Alkylbenzene Sulfonate (LAS)</text>

  <rect x="60" y="115" width="330" height="135" fill="#0f172a" rx="8"/>
  <text x="225" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Molecular Formula</text>
  <text x="225" y="165" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">CH3(CH2)11 — C6H4 — SO3- Na+</text>
  <!-- Tail, Benzene ring, Sulfonate -->
  <text x="225" y="195" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Long Hydrocarbon Tail + Benzene Ring + Sulfonate Head</text>
  <text x="225" y="220" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Polar -SO3- Na+ Group (Strong Electrolyte)</text>

  <rect x="60" y="265" width="330" height="140" fill="#0f172a" rx="6"/>
  <text x="225" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Two-Step Industrial Synthesis</text>
  <text x="225" y="315" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">1. Alkylation &amp; Sulfonation with Conc. H2SO4:</text>
  <text x="225" y="335" fill="#fbbf24" font-family="monospace" font-size="10" text-anchor="middle">R-C6H5 + H2SO4 --&gt; R-C6H4-SO3H + H2O</text>
  <text x="225" y="360" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2. Neutralization with Sodium Hydroxide:</text>
  <text x="225" y="380" fill="#4ade80" font-family="monospace" font-size="10" text-anchor="middle">R-C6H4-SO3H + NaOH --&gt; R-C6H4-SO3Na + H2O</text>

  <!-- Right: Why No Scum in Hard Water -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Why Soapless Detergents Resist Hard Water</text>

  <rect x="475" y="115" width="320" height="140" fill="#0f172a" rx="8"/>
  <text x="635" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Soluble Calcium &amp; Magnesium Salts</text>
  <text x="635" y="168" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">2R-SO3- Na+ + Ca2+ --&gt; (R-SO3)2Ca(aq) + 2Na+</text>
  <text x="635" y="195" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Calcium Sulfonate is 100% WATER-SOLUBLE</text>
  <text x="635" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">No precipitate (Scum) is ever formed!</text>

  <rect x="475" y="270" width="320" height="135" fill="#0f172a" rx="6"/>
  <text x="635" y="295" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Key Operational Advantages</text>
  <text x="635" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Lathers instantly in hard, cold, or acidic water</text>
  <text x="635" y="342" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Does not waste cleaning power neutralizing minerals</text>
  <text x="635" y="365" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Highly effective for delicate woolens and synthetics</text>
</svg>"""
    create_or_update_svg_block(l133, 3, 'Molecular Structure of Soapless Detergents, Two-Step Synthesis, and Hard Water Solubility', 'soapless_detergent_structure_133', svg_133)
    print()

    # =========================================================================
    # LESSON 134: Pollution Effect of Detergents
    # =========================================================================
    l134 = Lesson.objects.get(id=134)
    print(f'Enriching Lesson 134: \"{l134.title}\"')
    create_or_update_wm_block(
        l134, 2, 'Massive White Chemical Foam Blanket Covering River Water Surface Caused by Non-Biodegradable Detergents',
        'River_foam_pollution.jpg', 'US EPA', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:River_foam_pollution.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l134, 4, 'Dense Green Algal Bloom Eutrophication Choking Freshwater Lake Caused by Phosphate Builders',
        'Algal_bloom_eutrophication.jpg', 'Alexandre Roux', 'CC BY-SA 2.0',
        'https://commons.wikimedia.org/wiki/File:Algal_bloom_eutrophication.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_134 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Environmental Pollution by Detergents: Non-Biodegradability &amp; Eutrophication</text>

  <!-- Left: Biodegradability -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="225" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Molecular Branching &amp; Biodegradability</text>

  <rect x="60" y="115" width="330" height="95" fill="#0f172a" rx="8" stroke="#ef4444" stroke-width="1"/>
  <text x="75" y="138" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Branched Chain (ABS) — Non-Biodegradable</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Bacteria enzymes cannot break tertiary branch points</text>
  <text x="75" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11">Persists in waterways; causes persistent toxic river foam</text>

  <rect x="60" y="225" width="330" height="95" fill="#0f172a" rx="8" stroke="#4ade80" stroke-width="1"/>
  <text x="75" y="248" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Straight Chain (LAS) — Biodegradable</text>
  <text x="75" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Microorganisms digest straight hydrocarbon chains</text>
  <text x="75" y="290" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11">Decomposes rapidly in sewage treatment plants</text>

  <rect x="60" y="335" width="330" height="70" fill="#0f172a" rx="6"/>
  <text x="225" y="358" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Environmental Regulations (NEMA / Standards)</text>
  <text x="225" y="378" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Mandatory phase-out of non-biodegradable branched surfactants</text>

  <!-- Right: Eutrophication Cycle -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#fbbf24" stroke-width="2"/>
  <text x="635" y="95" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Phosphate Builder Eutrophication Cascade</text>

  <g transform="translate(475, 115)">
    <rect x="0" y="0" width="320" height="40" fill="#0f172a" rx="6" stroke="#fbbf24" stroke-width="1"/>
    <text x="160" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">1. Sodium Tripolyphosphate (STPP) in effluent</text>

    <rect x="0" y="55" width="320" height="40" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
    <text x="160" y="79" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">2. Explosive growth of Algal Blooms in water bodies</text>

    <rect x="0" y="110" width="320" height="40" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
    <text x="160" y="134" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">3. Sunlight blocked; submerged aquatic plants die</text>

    <rect x="0" y="165" width="320" height="40" fill="#0f172a" rx="6" stroke="#ef4444" stroke-width="1"/>
    <text x="160" y="189" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">4. Aerobic bacteria consume all Dissolved Oxygen (BOD)</text>

    <rect x="0" y="220" width="320" height="65" fill="#0f172a" rx="6" stroke="#a78bfa" stroke-width="1"/>
    <text x="160" y="245" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">5. Total Anoxia: Massive Fish Kills</text>
    <text x="160" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Solved by replacing phosphates with Zeolites &amp; Citrates</text>
  </g>
</svg>"""
    create_or_update_svg_block(l134, 3, 'Detergent Biodegradability Comparison and Phosphate-Induced Eutrophication Ecological Cascade', 'detergent_pollution_134', svg_134)
    print()

    # =========================================================================
    # LESSON 135: Polymers — Introduction
    # =========================================================================
    l135 = Lesson.objects.get(id=135)
    print(f'Enriching Lesson 135: \"{l135.title}\"')
    create_or_update_wm_block(
        l135, 2, 'Assorted Commercial Plastic Articles Displaying Standard Polymer Resin Identification Recycling Symbols (1-7)',
        'Plastic_resin_recycling_codes.jpg', 'Tomia', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Plastic_resin_recycling_codes.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l135, 3, 'Raw Natural Cotton Cellulose Fibres and Pure Silkworm Cocoon Filaments',
        'Cotton_boll_and_silk.jpg', 'Didier Descouens', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Cotton_boll_and_silk.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_135 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Fundamental Classification of Polymers: Origin, Synthesis &amp; Thermal Response</text>

  <g transform="translate(40, 65)">
    <!-- 1. Origin -->
    <rect x="0" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="122" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. By Origin / Source</text>
    <rect x="15" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="122" y="68" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Natural Polymers</text>
    <text x="122" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Cellulose, Starch, Wool, Silk, DNA</text>
    <text x="122" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Synthetic Polymers</text>
    <text x="122" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Polyethene, PVC, Nylon, Terylene</text>

    <!-- 2. Polymerization Method -->
    <rect x="270" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="392" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. By Polymerization Mode</text>
    <rect x="285" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="392" y="68" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Addition Polymerization</text>
    <text x="392" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Double bond opens (No byproduct)</text>
    <text x="392" y="115" fill="#f472b6" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Condensation Polymerization</text>
    <text x="392" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Functional groups link + H2O lost</text>

    <!-- 3. Thermal Behavior -->
    <rect x="540" y="0" width="245" height="170" fill="#1e293b" rx="10" stroke="#f87171" stroke-width="2"/>
    <text x="662" y="28" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. By Thermal Behavior</text>
    <rect x="555" y="45" width="215" height="110" fill="#0f172a" rx="6"/>
    <text x="662" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Thermoplastics</text>
    <text x="662" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Soften on heating &amp; recyclable (Polyethene)</text>
    <text x="662" y="115" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Thermosetting Plastics</text>
    <text x="662" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Cross-linked; char on heating (Bakelite)</text>

    <!-- Bottom: Definitions Summary -->
    <rect x="0" y="190" width="785" height="155" fill="#1e293b" rx="10" stroke="#64748b" stroke-width="1"/>
    <text x="392" y="215" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Monomer to Polymer Conversion Principle</text>
    <text x="392" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Monomer: A small, reactive molecule that can bind chemically to other molecules to form a polymer</text>
    <text x="392" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Polymer: A giant macromolecule composed of thousands of repeating structural units (monomers)</text>
    <text x="392" y="295" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Degree of Polymerization (n): Number of monomer units in a single chain (typically n = 500 to 50,000+)</text>
    <text x="392" y="325" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Molar Mass of Polymer = (Molar Mass of Repeating Unit) × n</text>
  </g>
</svg>"""
    create_or_update_svg_block(l135, 4, 'Polymer Classification Matrix: Natural vs Synthetic, Addition vs Condensation, and Thermal Properties', 'polymers_classification_135', svg_135)
    print()

    # =========================================================================
    # LESSON 136: Addition Polymerisation
    # =========================================================================
    l136 = Lesson.objects.get(id=136)
    print(f'Enriching Lesson 136: \"{l136.title}\"')
    create_or_update_wm_block(
        l136, 2, 'High-Density Polyethene (HDPE) White Plastic Pellets for Industrial Blow-Moulding',
        'HDPE_plastic_pellets.jpg', 'Cjp24', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:HDPE_plastic_pellets.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l136, 3, 'Clear Polyvinyl Chloride (PVC) Tubing and Insulated Electrical Cables',
        'PVC_tubing_sample.jpg', 'Santeri Viinamäki', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:PVC_tubing_sample.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_136 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Addition Polymerisation: Double Bond Cleavage &amp; Repeating Unit Formation</text>

  <!-- Top: General Reaction Mechanism -->
  <rect x="40" y="65" width="780" height="145" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
  <text x="430" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">General Addition Polymerisation Mechanism</text>

  <rect x="60" y="105" width="740" height="90" fill="#0f172a" rx="6"/>
  <text x="200" y="135" fill="#facc15" font-family="monospace" font-size="14" text-anchor="middle">n (CH2 = CH2)</text>
  <text x="200" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">n Monomers (Ethene)</text>

  <text x="380" y="145" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" text-anchor="middle">--[High P, T, Catalyst]--&gt;</text>

  <text x="600" y="135" fill="#4ade80" font-family="monospace" font-size="14" text-anchor="middle">— [— CH2 — CH2 —]n —</text>
  <text x="600" y="160" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Polyethene (Polymer)</text>
  <text x="600" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Double bond opens to form continuous single-bonded backbone</text>

  <!-- Bottom: 3 Classic Examples -->
  <g transform="translate(40, 225)">
    <!-- Polychloroethene (PVC) -->
    <rect x="0" y="0" width="245" height="205" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="122" y="25" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Polychloroethene (PVC)</text>
    <rect x="15" y="40" width="215" height="65" fill="#0f172a" rx="6"/>
    <text x="122" y="65" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Monomer: CH2 = CH(Cl)</text>
    <text x="122" y="88" fill="#fbbf24" font-family="monospace" font-size="11" text-anchor="middle">—[— CH2 — CH(Cl) —]n—</text>
    <rect x="15" y="115" width="215" height="80" fill="#0f172a" rx="6"/>
    <text x="122" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Key Applications:</text>
    <text x="122" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Water &amp; drainage pipes</text>
    <text x="122" y="173" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Electric cable insulation</text>
    <text x="122" y="190" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Artificial leather upholstery</text>

    <!-- Polyphenylethene (Polystyrene) -->
    <rect x="270" y="0" width="245" height="205" fill="#1e293b" rx="10" stroke="#f472b6" stroke-width="2"/>
    <text x="392" y="25" fill="#f472b6" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Polyphenylethene (Polystyrene)</text>
    <rect x="285" y="40" width="215" height="65" fill="#0f172a" rx="6"/>
    <text x="392" y="65" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Monomer: CH2 = CH(C6H5)</text>
    <text x="392" y="88" fill="#f472b6" font-family="monospace" font-size="11" text-anchor="middle">—[— CH2 — CH(C6H5) —]n—</text>
    <rect x="285" y="115" width="215" height="80" fill="#0f172a" rx="6"/>
    <text x="392" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Key Applications:</text>
    <text x="392" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Expanded foam packaging</text>
    <text x="392" y="173" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Disposable cups &amp; food boxes</text>
    <text x="392" y="190" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Refrigerator thermal insulation</text>

    <!-- Polytetrafluoroethene (Teflon) -->
    <rect x="540" y="0" width="245" height="205" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="662" y="25" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">PTFE (Teflon)</text>
    <rect x="555" y="40" width="215" height="65" fill="#0f172a" rx="6"/>
    <text x="662" y="65" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">Monomer: CF2 = CF2</text>
    <text x="662" y="88" fill="#4ade80" font-family="monospace" font-size="11" text-anchor="middle">—[— CF2 — CF2 —]n—</text>
    <rect x="555" y="115" width="215" height="80" fill="#0f172a" rx="6"/>
    <text x="662" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Key Applications:</text>
    <text x="662" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Non-stick cooking pans</text>
    <text x="662" y="173" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Chemical-resistant gaskets</text>
    <text x="662" y="190" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Low-friction machine bearings</text>
  </g>
</svg>"""
    create_or_update_svg_block(l136, 2, 'Addition Polymerisation Mechanism and Four Classic Industrial Addition Polymers', 'addition_polymers_136', svg_136)
    print()

    # =========================================================================
    # LESSON 137: Condensation Polymerisation
    # =========================================================================
    l137 = Lesson.objects.get(id=137)
    print(f'Enriching Lesson 137: \"{l137.title}\"')
    create_or_update_wm_block(
        l137, 2, 'Nylon Rope Trick Demonstration: Polymer Interface Film Continuous Thread Drawn from Immiscible Solutions',
        'Nylon_rope_trick_demo.jpg', 'Chemical Heritage Foundation', 'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Nylon_rope_trick_demo.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l137, 3, 'Polyethylene Terephthalate (PET / Terylene) Synthetic Polyester Textile Fabric Spools',
        'Polyester_fabric_yarn.jpg', 'Rama', 'CeCILL',
        'https://commons.wikimedia.org/wiki/File:Polyester_fabric_yarn.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_137 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 460" width="100%" height="100%">
  <rect width="860" height="460" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Condensation Polymerisation: Amide &amp; Ester Linkages with Elimination of Water</text>

  <!-- Left: Polyamide (Nylon 6,6) -->
  <rect x="40" y="65" width="370" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Polyamide: Nylon-6,6</text>

  <rect x="60" y="115" width="330" height="150" fill="#0f172a" rx="8"/>
  <text x="225" y="138" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Monomers: Hexanedioic Acid + 1,6-Diaminohexane</text>
  <text x="225" y="165" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">HOOC-(CH2)4-COOH + H2N-(CH2)6-NH2 --&gt;</text>
  
  <rect x="75" y="180" width="300" height="45" fill="#1e293b" rx="4"/>
  <text x="225" y="200" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">—[— CO(CH2)4CO — NH(CH2)6NH —]n—</text>
  <text x="225" y="218" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">+ 2n H2O  (Amide / Peptide Link: -CO-NH-)</text>

  <rect x="60" y="280" width="330" height="135" fill="#0f172a" rx="6"/>
  <text x="225" y="305" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Nylon Properties &amp; Uses</text>
  <text x="225" y="328" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Very high tensile strength &amp; elasticity</text>
  <text x="225" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Resists abrasion, fungal rot, and moths</text>
  <text x="225" y="372" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Climbing ropes, fishing nets, toothbrushes</text>
  <text x="225" y="395" fill="#facc15" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Synthetic analog of natural protein fibres</text>

  <!-- Right: Polyester (Terylene / PET) -->
  <rect x="450" y="65" width="370" height="365" fill="#1e293b" rx="12" stroke="#f472b6" stroke-width="2"/>
  <text x="635" y="95" fill="#f472b6" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Polyester: Terylene (PET)</text>

  <rect x="475" y="115" width="320" height="150" fill="#0f172a" rx="8"/>
  <text x="635" y="138" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Monomers: Benzene-1,4-dicarboxylic Acid + Ethane-1,2-diol</text>
  <text x="635" y="165" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">HOOC-C6H4-COOH + HO-CH2CH2-OH --&gt;</text>
  
  <rect x="490" y="180" width="290" height="45" fill="#1e293b" rx="4"/>
  <text x="635" y="200" fill="#f472b6" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">—[— CO-C6H4-CO — O-CH2CH2-O —]n—</text>
  <text x="635" y="218" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">+ 2n H2O  (Ester Link: -COO-)</text>

  <rect x="475" y="280" width="320" height="135" fill="#0f172a" rx="6"/>
  <text x="635" y="305" fill="#f472b6" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Terylene Properties &amp; Uses</text>
  <text x="635" y="328" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Wrinkle-resistant &amp; dries rapidly</text>
  <text x="635" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Blended with cotton (Polycotton shirts)</text>
  <text x="635" y="372" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• PET beverage bottles, sailcloth, tyre cords</text>
  <text x="635" y="395" fill="#facc15" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">100% recyclable thermoplastic polyester</text>
</svg>"""
    create_or_update_svg_block(l137, 4, 'Condensation Polymerisation Mechanism for Nylon 6,6 and Terylene with Ester and Amide Linkages', 'condensation_polymers_137', svg_137)
    print()

    # =========================================================================
    # LESSON 138: Natural Polymers and Fibres
    # =========================================================================
    l138 = Lesson.objects.get(id=138)
    print(f'Enriching Lesson 138: \"{l138.title}\"')
    create_or_update_wm_block(
        l138, 2, 'Natural Mature Cotton Bolls (Gossypium) Showing Pure Cellulose Fibres',
        'Cotton_bolls_ready_for_harvest.jpg', 'Kimberly Vardeman', 'CC BY 2.0',
        'https://commons.wikimedia.org/wiki/File:Cotton_bolls_ready_for_harvest.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l138, 3, 'Raw Sheep Fleece Wool Showing Crimped Keratin Protein Fibres',
        'Wool_fleece_raw.jpg', 'Agricultural Research Service', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Wool_fleece_raw.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_138 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Four Essential Classes of Natural Polymers: Structure &amp; Biological Roles</text>

  <g transform="translate(40, 65)">
    <!-- Cellulose & Starch -->
    <rect x="0" y="0" width="370" height="170" fill="#1e293b" rx="10" stroke="#4ade80" stroke-width="2"/>
    <text x="185" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Polysaccharides: Starch &amp; Cellulose</text>
    <rect x="15" y="45" width="340" height="110" fill="#0f172a" rx="6"/>
    <text x="185" y="68" fill="#facc15" font-family="monospace" font-size="11" text-anchor="middle">Monomer: Glucose (C6H12O6) --&gt; (C6H10O5)n</text>
    <text x="185" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Starch: α-glucose storage polymer in plants</text>
    <text x="185" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cellulose: β-glucose structural polymer in plant cell walls</text>
    <text x="185" y="132" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Cotton = 90% pure cellulose; paper &amp; rayon feedstock</text>

    <!-- Proteins -->
    <rect x="410" y="0" width="370" height="170" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="595" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Polypeptides: Proteins (Silk, Wool)</text>
    <rect x="425" y="45" width="340" height="110" fill="#0f172a" rx="6"/>
    <text x="595" y="68" fill="#facc15" font-family="monospace" font-size="11" text-anchor="middle">Monomer: Amino Acids (H2N-CHR-COOH)</text>
    <text x="595" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Linked by Peptide bonds (-CO-NH-) + H2O lost</text>
    <text x="595" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Wool (Keratin): Contains sulfur cross-links</text>
    <text x="595" y="132" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Silk (Fibroin): High tensile strength natural filament</text>

    <!-- Nucleic Acids -->
    <rect x="0" y="190" width="370" height="165" fill="#1e293b" rx="10" stroke="#f472b6" stroke-width="2"/>
    <text x="185" y="218" fill="#f472b6" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. Polynucleotides: DNA &amp; RNA</text>
    <rect x="15" y="235" width="340" height="105" fill="#0f172a" rx="6"/>
    <text x="185" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Monomer: Nucleotides (Sugar + Base + Phosphate)</text>
    <text x="185" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Stores &amp; transmits genetic information in cells</text>
    <text x="185" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Double helix stabilized by complementary H-bonds</text>
    <text x="185" y="322" fill="#f472b6" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Directs protein synthesis in living organisms</text>

    <!-- Natural Rubber -->
    <rect x="410" y="190" width="370" height="165" fill="#1e293b" rx="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="595" y="218" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4. Polyisoprene: Natural Rubber</text>
    <rect x="425" y="235" width="340" height="105" fill="#0f172a" rx="6"/>
    <text x="595" y="258" fill="#facc15" font-family="monospace" font-size="11" text-anchor="middle">Monomer: 2-Methylbuta-1,3-diene (Isoprene)</text>
    <text x="595" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• cis-1,4-polyisoprene polymer tapped as latex sap</text>
    <text x="595" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Coagulated with methanoic/ethanoic acid</text>
    <text x="595" y="322" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Elastic but soft; modified via vulcanisation</text>
  </g>
</svg>"""
    create_or_update_svg_block(l138, 4, 'Classification and Biochemical Structures of Four Essential Classes of Natural Polymers', 'natural_polymers_138', svg_138)
    print()

    # =========================================================================
    # LESSON 139: Rubber and Vulcanisation
    # =========================================================================
    l139 = Lesson.objects.get(id=139)
    print(f'Enriching Lesson 139: \"{l139.title}\"')
    create_or_update_wm_block(
        l139, 2, 'White Latex Milky Sap Being Tapped from Trunk of Hevea brasiliensis Rubber Tree',
        'Rubber_tree_latex_tapping.jpg', 'Fir0002', 'GFDL 1.2',
        'https://commons.wikimedia.org/wiki/File:Rubber_tree_latex_tapping.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l139, 3, 'Heavy-Duty Automotive Vehicle Tyre Manufactured from Tough Cross-Linked Vulcanised Rubber',
        'Car_tyre_tread.jpg', 'Santeri Viinamäki', 'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Car_tyre_tread.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_139 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Chemistry of Vulcanisation: Sulfur Cross-Linking in Polyisoprene Rubber</text>

  <!-- Left: Raw vs Vulcanised Lattice -->
  <rect x="40" y="65" width="460" height="355" fill="#1e293b" rx="12" stroke="#fbbf24" stroke-width="2"/>
  <text x="270" y="95" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Molecular Cross-Link Mechanism</text>

  <g transform="translate(65, 120)">
    <rect x="0" y="0" width="410" height="150" fill="#0f172a" rx="8"/>
    <!-- Chain 1 -->
    <path d="M 20 40 Q 70 20 120 40 T 220 40 T 320 40 T 390 40" stroke="#38bdf8" stroke-width="4" fill="none"/>
    <text x="200" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Polyisoprene Chain 1</text>

    <!-- Sulfur bridges -->
    <line x1="120" y1="40" x2="120" y2="105" stroke="#facc15" stroke-width="3" stroke-dasharray="2"/>
    <text x="135" y="75" fill="#facc15" font-family="monospace" font-size="11" font-weight="bold">-S-S-</text>

    <line x1="260" y1="40" x2="260" y2="105" stroke="#facc15" stroke-width="3" stroke-dasharray="2"/>
    <text x="275" y="75" fill="#facc15" font-family="monospace" font-size="11" font-weight="bold">-S-S-</text>

    <!-- Chain 2 -->
    <path d="M 20 105 Q 70 85 120 105 T 220 105 T 320 105 T 390 105" stroke="#4ade80" stroke-width="4" fill="none"/>
    <text x="200" y="130" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Polyisoprene Chain 2</text>
  </g>

  <rect x="60" y="285" width="420" height="120" fill="#0f172a" rx="6"/>
  <text x="270" y="310" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Charles Goodyear Process (Heating with Sulfur at 140°C)</text>
  <text x="270" y="332" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Sulfur atoms react across double bonds of adjacent chains</text>
  <text x="270" y="352" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Disulfide (-S-S-) bridges prevent chains from slipping permanently</text>
  <text x="270" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">• Chains spring back immediately upon release of stretching stress</text>

  <!-- Right: Property Comparison Table -->
  <rect x="520" y="65" width="300" height="355" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="670" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Property Improvements</text>

  <rect x="540" y="115" width="260" height="135" fill="#0f172a" rx="6" stroke="#f87171" stroke-width="1"/>
  <text x="670" y="138" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Raw Natural Rubber</text>
  <text x="670" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Soft &amp; sticky when warm (&gt;30°C)</text>
  <text x="670" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Brittle &amp; stiff when cold (&lt;10°C)</text>
  <text x="670" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Readily oxidized by air/ozone</text>
  <text x="670" y="220" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">• Low tensile strength &amp; wears out fast</text>

  <rect x="540" y="265" width="260" height="140" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
  <text x="670" y="288" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Vulcanised Rubber</text>
  <text x="670" y="310" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Retains elasticity over -40°C to 100°C</text>
  <text x="670" y="330" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Tough, abrasion &amp; tear-resistant</text>
  <text x="670" y="350" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Resistant to organic solvents &amp; weathering</text>
  <text x="670" y="375" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Automotive tyres, belts, soles, hoses</text>
</svg>"""
    create_or_update_svg_block(l139, 4, 'Vulcanisation Sulfur Cross-Linking Chemistry and Comparative Mechanical Properties', 'vulcanisation_rubber_139', svg_139)
    print()

    # =========================================================================
    # LESSON 140: Advantages, Disadvantages & Pollution Effects of Synthetic Polymers
    # =========================================================================
    l140 = Lesson.objects.get(id=140)
    print(f'Enriching Lesson 140: \"{l140.title}\"')
    create_or_update_wm_block(
        l140, 2, 'Plastic Debris Accumulation Along Marine Shoreline Highlighting Non-Biodegradability Problem',
        'Marine_plastic_pollution.jpg', 'NOAA Marine Debris Program', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Marine_plastic_pollution.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Crystals_Halite_on_matrix.jpg'
    )
    create_or_update_wm_block(
        l140, 3, 'Industrial Plastic Flake Mechanical Sorting and Recycling Pelletizing Facility',
        'Plastic_recycling_facility.jpg', 'US Air Force', 'Public domain',
        'https://commons.wikimedia.org/wiki/File:Plastic_recycling_facility.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/9/90/Sodium_metal_in_oil.jpg'
    )
    svg_140 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 450" width="100%" height="100%">
  <rect width="860" height="450" fill="#0a0f1d" rx="16"/>
  <text x="430" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Synthetic Polymer Life Cycle: Environmental Challenges &amp; Circular Solutions</text>

  <!-- Left: Environmental Hazards -->
  <rect x="40" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="2"/>
  <text x="225" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Environmental &amp; Health Hazards</text>

  <rect x="60" y="115" width="330" height="85" fill="#0f172a" rx="6" stroke="#ef4444" stroke-width="1"/>
  <text x="75" y="138" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Non-Biodegradability (Hundreds of Years)</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Inert C-C bonds resist bacterial decomposers</text>
  <text x="75" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11">Clogs storm drains, chokes livestock &amp; marine life</text>

  <rect x="60" y="215" width="330" height="85" fill="#0f172a" rx="6" stroke="#f97316" stroke-width="1"/>
  <text x="75" y="238" fill="#f97316" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Toxic Gas Release Upon Incineration</text>
  <text x="75" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Burning PVC releases corrosive HCl &amp; toxic Dioxins</text>
  <text x="75" y="280" fill="#fed7aa" font-family="system-ui, sans-serif" font-size="11">Polyurethanes release lethal Hydrogen Cyanide (HCN)</text>

  <rect x="60" y="315" width="330" height="90" fill="#0f172a" rx="6"/>
  <text x="225" y="340" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Microplastics &amp; Bioaccumulation</text>
  <text x="225" y="362" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">UV fragmentation produces microplastics (&lt;5mm)</text>
  <text x="225" y="385" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Infiltrates marine food webs and human drinking water</text>

  <!-- Right: Sustainable Solutions -->
  <rect x="450" y="65" width="370" height="355" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="2"/>
  <text x="635" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Circular Waste Management Hierarchy</text>

  <g transform="translate(475, 115)">
    <rect x="0" y="0" width="320" height="50" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1"/>
    <text x="160" y="22" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">1. Reduce &amp; Replace with Bioplastics</text>
    <text x="160" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Polylactic acid (PLA) &amp; corn starch biopolymers</text>

    <rect x="0" y="65" width="320" height="50" fill="#0f172a" rx="6" stroke="#38bdf8" stroke-width="1"/>
    <text x="160" y="87" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">2. Closed-Loop Mechanical Recycling</text>
    <text x="160" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Automated optical sorting, shredding, and remelting</text>

    <rect x="0" y="130" width="320" height="50" fill="#0f172a" rx="6" stroke="#facc15" stroke-width="1"/>
    <text x="160" y="152" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">3. Pyrolysis &amp; Chemical Recycling</text>
    <text x="160" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Thermal cracking back into monomer hydrocarbon fuels</text>

    <rect x="0" y="195" width="320" height="90" fill="#0f172a" rx="6" stroke="#a78bfa" stroke-width="1"/>
    <text x="160" y="220" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">4. Legislative Policy &amp; Extended Producer Responsibility</text>
    <text x="160" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Nationwide bans on single-use plastic carrier bags</text>
    <text x="160" y="265" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">• Deposit refund schemes &amp; circular economy tax credits</text>
  </g>
</svg>"""
    create_or_update_svg_block(l140, 4, 'Synthetic Polymer Environmental Impact, Microplastic Hazards, and Circular Recycling Hierarchy', 'polymer_pollution_solutions_140', svg_140)
    print()

    print('=== Second Half of Topic 6 (Lessons 129 - 140) Completed Successfully! ===')

if __name__ == '__main__':
    enrich_topic6_second_half()
