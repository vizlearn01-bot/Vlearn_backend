import os
import sys
import django
import requests
import re
import time

sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset

HEADERS = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}

def search_wikimedia_thumb(query):
    api_url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrnamespace': 6,
        'gsrsearch': query,
        'gsrlimit': 5,
        'prop': 'imageinfo',
        'iiprop': 'url|mime|extmetadata',
        'iiurlwidth': 960,
        'format': 'json',
    }
    try:
        r = requests.get(api_url, params=params, headers=HEADERS, timeout=8)
        if r.status_code == 200:
            pages = r.json().get('query', {}).get('pages', {})
            for pdata in pages.values():
                if 'imageinfo' in pdata and pdata['imageinfo']:
                    info = pdata['imageinfo'][0]
                    mime = info.get('mime', '')
                    if mime in ['image/jpeg', 'image/png', 'image/webp']:
                        thumb = info.get('thumburl') or info.get('url')
                        meta = info.get('extmetadata', {})
                        author = meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                        author = re.sub(r'<[^>]+>', '', author).strip()
                        lic = meta.get('LicenseShortName', {}).get('value', 'CC BY-SA')
                        clean_url = thumb.split('?')[0] if '?' in thumb else thumb
                        return {
                            'url': clean_url,
                            'commons_url': info.get('descriptionurl'),
                            'author': author or 'Wikimedia Contributor',
                            'licensing': lic or 'Creative Commons',
                            'title': pdata.get('title', '').replace('File:', '')
                        }
    except Exception as e:
        print(f'Error searching {query}: {e}')
    return None

TOPIC7_ASSET_MAPPING = {
    141: [
        ('Autunite mineral', 'Natural Autunite / Pitchblende radioactive mineral specimen', 2),
        ('CEC Model 21-101 mass spectrometer', 'Mass Spectrometer laboratory instrument used to determine isotopic masses and abundances', 3),
    ],
    142: [
        ('Nuclear binding energy curve', 'Nuclear Binding Energy per Nucleon curve illustrating maximum stability near Iron-56', 2),
        ('Mass defect nuclear', 'Visual representation of nuclear mass defect and binding energy equivalent', 3),
    ],
    143: [
        ('Becquerel rays', 'Historical Becquerel uranium salt photographic plate demonstrating spontaneous radioactivity', 2),
        ('Pitchblende mineral', 'Uranium ore (Pitchblende) emitting spontaneous ionizing radiation', 3),
    ],
    144: [
        ('Marie Curie laboratory', 'Marie and Pierre Curie historical radioactivity research laboratory setup', 2),
        ('Gold leaf electroscope', 'Historical gold-leaf electroscope used to detect radiation ionization in air', 3),
    ],
    145: [
        ('Cloud chamber tracks', 'Wilson Cloud Chamber showing thick, dense ionization tracks of Alpha particles', 2),
        ('Radiation penetration Alpha Beta Gamma', 'Standard diagram showing penetration depths of Alpha, Beta, and Gamma rays', 3),
    ],
    146: [
        ('Lead shielding nuclear', 'Dense lead brick wall shielding radiation in high-activity radiochemistry facility', 2),
        ('Geiger counter radiation', 'Geiger-Müller survey meter detecting environmental and sample radiation counts', 3),
    ],
    147: [
        ('Cathode ray deflection', 'Cathode ray beam deflected in electric and magnetic fields', 2),
        ('Electromagnet physics laboratory', 'Laboratory electromagnet pole pieces creating uniform magnetic field for particle deflection', 3),
    ],
    148: [
        ('Ionization chamber', 'Ionization chamber instrument demonstrating ion pair collection from radiation', 2),
        ('Smoke detector mechanism', 'Americium-241 ionization smoke detector core showing alpha ionization mechanism', 3),
    ],
    149: [
        ('Radioactive decay curve', 'Exponential radioactive decay curve showing activity reduction per half-life interval', 2),
        ('Mass spectrometry laboratory', 'Accelerator Mass Spectrometry (AMS) facility for Carbon-14 archaeological dating', 3),
    ],
    150: [
        ('Alpha decay', 'Nuclear Alpha decay illustration showing emission of Helium-4 nucleus', 2),
        ('Beta decay', 'Nuclear Beta-minus decay reaction transforming a neutron into a proton and electron', 3),
    ],
    151: [
        ('Thorium mineral', 'Pure Thorium Nitrate compound exhibiting natural alpha and beta radioactivity', 2),
        ('Nuclear track detector', 'Solid-state nuclear track etch detector used to measure radon gas emissions', 3),
    ],
    152: [
        ('Nuclear power plant cooling towers', 'Pressurized Water Reactor (PWR) nuclear power station with containment dome', 2),
        ('Cherenkov radiation reactor pool', 'Luminous blue Cherenkov radiation glow in nuclear research reactor core pool', 3),
    ],
    153: [
        ('Sun solar flare', 'Thermonuclear fusion in the Sun observed via NASA Solar Dynamics Observatory', 2),
        ('Tokamak fusion reactor', 'Toroidal Tokamak magnetic confinement fusion reactor vacuum vessel interior', 3),
    ],
    154: [
        ('Gamma radiography weld', 'Industrial gamma radiography camera inspecting structural steel weld joints', 2),
        ('Cobalt-60 radiation', 'Commercial food irradiation facility utilizing Cobalt-60 gamma radiation', 3),
    ],
    155: [
        ('PET scanner hospital', 'Clinical Positron Emission Tomography (PET-CT) imaging suite in hospital', 2),
        ('Autoradiography plant', 'Autoradiograph visualizing Phosphorus-32 radioactive tracer uptake in plants', 3),
    ],
    156: [
        ('Radiation warning symbol', 'Universal international ionizing radiation hazard trefoil warning symbol', 2),
        ('Radiation dosimeter badge', 'Personal thermoluminescent dosimeter (TLD) badge worn by radiation workers', 3),
    ],
    157: [
        ('Chernobyl new safe confinement', 'New Safe Confinement arch shelter over damaged Chernobyl Reactor 4', 2),
        ('Radioactive waste cask', 'Vitrified high-level nuclear waste steel canister storage facility', 3),
    ],
    158: [
        ('IAEA seal', 'International Atomic Energy Agency (IAEA) tamper-evident nuclear containment seal', 2),
        ('Radiation protection suit', 'Radiation worker in full protective hazmat PPE suit conducting contamination survey', 3),
    ],
}

def run_fix():
    print('Starting Topic 7 verified Wikimedia CDN thumbnail repair...')
    total_repaired = 0

    for lesson_id, mappings in TOPIC7_ASSET_MAPPING.items():
        try:
            lesson = Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExist:
            print(f'Lesson {lesson_id} does not exist.')
            continue

        for search_query, asset_title, page_num in mappings:
            data = search_wikimedia_thumb(search_query)
            if not data:
                short_q = search_query.split()[0]
                data = search_wikimedia_thumb(short_q)

            if not data:
                print(f'Could not find Wikimedia asset for {search_query} (Lesson {lesson_id})')
                continue

            # 1. Update or create corresponding LessonBlock on page_num
            block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
            if block and block.assets.filter(source_type='ai_generated').exists():
                block = None

            if not block:
                block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_type='suggested_diagram',
                    title=asset_title,
                    content={
                        'title': asset_title,
                        'caption': asset_title,
                        'url': data['url'],
                        'resolved_image_url': data['url']
                    },
                    order=0,
                    page_number=page_num,
                    page_title=None
                )
            else:
                block.title = asset_title
                if isinstance(block.content, dict):
                    block.content['title'] = asset_title
                    block.content['caption'] = asset_title
                    block.content['url'] = data['url']
                    block.content['resolved_image_url'] = data['url']
                block.save()

            # 2. Update or create LessonAsset
            asset = block.assets.filter(source_type='external').first()
            if asset:
                asset.title = asset_title
                asset.description = f'Wikimedia Commons photographic asset: {asset_title}'
                asset.url = data['url']
                asset.metadata = {
                    'author': data['author'],
                    'licensing': data['licensing'],
                    'commons_page_url': data['commons_url']
                }
                asset.save()
            else:
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type='image',
                    source_type='external',
                    storage_type='url',
                    title=asset_title,
                    description=f'Wikimedia Commons photographic asset: {asset_title}',
                    url=data['url'],
                    metadata={
                        'author': data['author'],
                        'licensing': data['licensing'],
                        'commons_page_url': data['commons_url']
                    },
                    status='approved'
                )
                asset.blocks.add(block)
            total_repaired += 1
            print(f'Lesson {lesson_id} [P{page_num}]: {asset_title} -> {data["url"]}')
            time.sleep(0.3)

    print(f'Done! Successfully repaired {total_repaired} Wikimedia thumbnail assets in Topic 7.')

if __name__ == '__main__':
    run_fix()
