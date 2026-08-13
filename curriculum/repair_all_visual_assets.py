import os
import sys
import re
import requests
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

WIKIMEDIA_USER_AGENT = 'VlearnCurriculumBot/1.0 (https://vlearn.org; contact@vlearn.org)'
headers = {'User-Agent': WIKIMEDIA_USER_AGENT}

def get_wikimedia_working_url(filename_or_url, commons_page=None):
    filename = None
    if commons_page:
        m = re.search(r'File:(.+)$', commons_page)
        if m:
            filename = m.group(1).strip()
    
    if not filename and filename_or_url:
        parts = filename_or_url.split('/')
        if 'thumb' in filename_or_url:
            if len(parts) >= 2:
                filename = parts[-2]
        else:
            filename = parts[-1]
            if '?' in filename:
                filename = filename.split('?')[0]

    if not filename:
        return None

    api_url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'titles': f'File:{filename}',
        'prop': 'imageinfo',
        'iiprop': 'url|size|mime',
        'iiurlwidth': 800,
        'format': 'json',
    }
    try:
        resp = requests.get(api_url, params=params, headers=headers, timeout=8)
        if resp.status_code == 200:
            data = resp.json()
            pages = data.get('query', {}).get('pages', {})
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

    if filename_or_url:
        m = re.match(r'^(https://upload\.wikimedia\.org/wikipedia/commons)/thumb/([0-9a-f]/[0-9a-f]{2}/[^/]+)/.+$', filename_or_url)
        if m:
            raw_constructed = f'{m.group(1)}/{m.group(2)}'
            try:
                r = requests.head(raw_constructed, headers=headers, timeout=4)
                if r.status_code == 200:
                    return raw_constructed
            except Exception:
                pass

    return None

def repair_all_wikimedia_assets():
    print('=== REPAIRING ALL WIKIMEDIA ASSETS ===')
    assets = LessonAsset.objects.filter(source_type='external').exclude(url__isnull=True).exclude(url='')
    repaired_count = 0
    already_good = 0
    failed_count = 0

    for a in assets:
        current_url = a.url
        try:
            r = requests.head(current_url, headers=headers, timeout=4)
            if r.status_code == 200:
                already_good += 1
                # Sync to block content
                for b in a.blocks.all():
                    if isinstance(b.content, dict) and b.content.get('resolved_image_url') != current_url:
                        b.content['resolved_image_url'] = current_url
                        b.content['url'] = current_url
                        b.save(update_fields=['content'])
                continue
        except Exception:
            pass

        print(f'Repairing Asset {a.id} (Lesson {a.lesson_id}): current URL failed ({current_url[:60]}...)')
        commons_page = a.metadata.get('commons_page_url') if a.metadata else None
        working_url = get_wikimedia_working_url(current_url, commons_page)

        if working_url:
            print(f'  -> Found working URL: {working_url[:70]}...')
            a.url = working_url[:200]
            a.save(update_fields=['url'])
            repaired_count += 1
            for b in a.blocks.all():
                if isinstance(b.content, dict):
                    b.content['resolved_image_url'] = working_url
                    b.content['url'] = working_url
                    b.save(update_fields=['content'])
        else:
            print(f'  -> FAILED to find working URL for Asset {a.id}')
            failed_count += 1

    print(f'Wikimedia assets summary: {already_good} already working, {repaired_count} repaired, {failed_count} failed.\n')

if __name__ == '__main__':
    repair_all_wikimedia_assets()
