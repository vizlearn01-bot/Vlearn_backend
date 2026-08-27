"""
Automatic Wikimedia image fetcher and verifier for Grade 10 Geography Topics 1 & 2.
"""

import os
import sys
import json
import requests

headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}

def search_wikimedia(queries):
    url = 'https://commons.wikimedia.org/w/api.php'
    
    for q in queries:
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': f'{q} filetype:bitmap',
            'srnamespace': 6,
            'srlimit': 8,
            'format': 'json'
        }
        try:
            r = requests.get(url, params=params, headers=headers, timeout=10)
            data = r.json()
            items = data.get('query', {}).get('search', [])
            if not items:
                continue
            
            valid_titles = [
                item['title'] for item in items 
                if not any(item['title'].lower().endswith(ext) for ext in ['.tif', '.tiff', '.pdf', '.svg', '.gif', '.webm', '.ogv'])
            ]
            if not valid_titles:
                continue

            info_params = {
                'action': 'query',
                'titles': '|'.join(valid_titles[:5]),
                'prop': 'imageinfo',
                'iiprop': 'url|size|extmetadata',
                'format': 'json'
            }
            r_info = requests.get(url, params=info_params, headers=headers, timeout=10)
            info_data = r_info.json()

            for pid, page in info_data.get('query', {}).get('pages', {}).items():
                if 'imageinfo' in page and page['imageinfo']:
                    ii = page['imageinfo'][0]
                    raw_url = ii['url']
                    clean_url = raw_url.split('?')[0]
                    size = ii.get('size', 0)
                    meta = ii.get('extmetadata', {})
                    
                    author = meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                    license_name = meta.get('LicenseShortName', {}).get('value', 'CC BY-SA')
                    desc = meta.get('ImageDescription', {}).get('value', '')

                    if size > 15000:
                        try:
                            test_r = requests.get(clean_url, headers=headers, timeout=8)
                            if test_r.status_code == 200 and len(test_r.content) > 10000:
                                return {
                                    'title': page['title'],
                                    'url': clean_url,
                                    'commons_url': f"https://commons.wikimedia.org/wiki/{page['title'].replace(' ', '_')}",
                                    'author': author[:100],
                                    'licensing': license_name[:50],
                                    'matched_query': q
                                }
                        except Exception:
                            continue
        except Exception as err:
            print(f"Query error {q}: {err}")
            continue
    return None

TOPIC_1_QUERIES = {
    1: ["Great Rift Valley Kenya landscape", "East African Rift landscape", "Rift Valley Kenya viewpoint"],
    2: ["Kericho tea farm plantation", "Mount Kenya forest slopes landscape", "Highland agriculture Kenya"],
    3: ["Standard Gauge Railway Kenya train landscape", "Nairobi infrastructure SGR", "Railway bridge Kenya"],
    4: ["Mau Forest Kenya trees river", "Aberdare National Park waterfall forest", "Mount Kenya forest stream"],
    5: ["Surveyor total station tripods", "Geologist field measuring compass", "Land surveyor instrument field"],
    6: ["Meteorological station weather instruments", "Automatic weather station anemometer", "Meteorology instruments Stevenson screen"],
    7: ["Fieldwork geography students mapping", "Students measuring outdoors survey", "School field study geography"],
    8: ["Mount Kenya peaks landscape", "Kenya landscape aerial highlands", "Great Rift Valley panorama"]
}

TOPIC_2_QUERIES = {
    1: ["Topographic map sheet contours", "Topographical survey map paper", "Ordnance survey map contour lines"],
    2: ["Magnetic compass bearing map", "Prismatic compass map navigation", "Compass on topographic map"],
    3: ["Map scale measurement ruler", "Measuring distance on map thread", "Topographic map measuring scale"],
    4: ["Map legend symbols key", "Topographic map symbols legend", "Cartography map signs legend"],
    5: ["Grid reference map coordinates", "National grid coordinates map", "Map reading grid lines"],
    6: ["Trig point triangulation pillar", "Triangulation station benchmark survey", "Survey benchmark stone"],
    7: ["Contour lines steep mountain relief", "Contour terrain topography model", "Mountain contour relief map"],
    8: ["Dendritic drainage river network aerial", "River drainage basin tributaries aerial", "Meandering river aerial view"],
    9: ["Tropical forest canopy landscape aerial", "Savanna grassland acacia Kenya", "Mangrove forest coastline aerial"],
    10: ["Rift valley escarpment vegetation landscape", "Highland terrain drainage forest Kenya", "Mountain valley river vegetation"],
    11: ["Topographical profile cross section", "Geological cross section topography", "Elevation profile surveying"],
    12: ["Road construction mountain pass route", "Pipeline route construction terrain", "Infrastructure route planning landscape"],
    13: ["Topographic map reading examination", "Cartographer analyzing map survey", "Geographic map interpretation work"]
}

def main():
    results_t1 = {}
    print("=== Fetching Topic 1 Images ===")
    for lesson_num, queries in TOPIC_1_QUERIES.items():
        res = search_wikimedia(queries)
        print(f"Topic 1 Lesson {lesson_num}: {res.get('url') if res else 'FAILED'}")
        results_t1[lesson_num] = res

    with open('curriculum/grade10_geography_topic1_verified_images.json', 'w') as f:
        json.dump(results_t1, f, indent=2)

    results_t2 = {}
    print("\n=== Fetching Topic 2 Images ===")
    for lesson_num, queries in TOPIC_2_QUERIES.items():
        res = search_wikimedia(queries)
        print(f"Topic 2 Lesson {lesson_num}: {res.get('url') if res else 'FAILED'}")
        results_t2[lesson_num] = res

    with open('curriculum/grade10_geography_topic2_verified_images.json', 'w') as f:
        json.dump(results_t2, f, indent=2)

    print("\nSaved verified images to JSON.")

if __name__ == '__main__':
    main()
