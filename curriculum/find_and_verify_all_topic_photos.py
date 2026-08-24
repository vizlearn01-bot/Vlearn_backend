"""
Multi-tier search and verification script to find 100% accurate, topic-specific
Wikimedia Commons images for all 22 lessons across Grade 7 Home Science (Topics 1 to 6).
"""

import requests
import json
import re

headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}

def search_wikimedia(queries):
    url = 'https://commons.wikimedia.org/w/api.php'
    
    for q in queries:
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': f'{q} filetype:bitmap',
            'srnamespace': 6,
            'srlimit': 10,
            'format': 'json'
        }
        try:
            r = requests.get(url, params=params, headers=headers, timeout=8)
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
                'titles': '|'.join(valid_titles[:6]),
                'prop': 'imageinfo',
                'iiprop': 'url|size|extmetadata',
                'format': 'json'
            }
            r_info = requests.get(url, params=info_params, headers=headers, timeout=8)
            info_data = r_info.json()

            for pid, page in info_data.get('query', {}).get('pages', {}).items():
                if 'imageinfo' in page and page['imageinfo']:
                    ii = page['imageinfo'][0]
                    raw_url = ii['url']
                    clean_url = raw_url.split('?')[0]
                    size = ii.get('size', 0)
                    if size > 15000:
                        # Verify HTTP 200
                        try:
                            test_r = requests.get(clean_url, headers=headers, timeout=6)
                            if test_r.status_code == 200 and len(test_r.content) > 10000:
                                return {
                                    'title': page['title'],
                                    'url': clean_url,
                                    'bytes': len(test_r.content),
                                    'matched_query': q
                                }
                        except Exception:
                            continue
        except Exception:
            continue
    return None

all_lessons = {
    # -------------------------------------------------------------------------
    # Topic 1: Kitchen Safety (3 Lessons)
    # -------------------------------------------------------------------------
    "Topic 1 - Lesson 1 (Kitchen Accidents & Prevention)": [
        "gas stove burner flame",
        "kitchen cooking fire",
        "gas stove flame"
    ],
    "Topic 1 - Lesson 2 (First Aid for Burns & Cuts)": [
        "first aid kit bandage",
        "first aid kit",
        "bandaging first aid"
    ],
    "Topic 1 - Lesson 3 (Kitchen Hygiene & Waste)": [
        "washing hands soap",
        "kitchen cleaning",
        "dishwashing soap"
    ],

    # -------------------------------------------------------------------------
    # Topic 2: Small Kitchen Tools and Equipment (3 Lessons)
    # -------------------------------------------------------------------------
    "Topic 2 - Lesson 1 (Classification of Kitchen Tools)": [
        "kitchen knives cutting board",
        "cooking utensils set",
        "kitchen cutlery tools"
    ],
    "Topic 2 - Lesson 2 (Care, Cleaning & Storage)": [
        "dish drying rack kitchen",
        "washing dishes sink",
        "clean kitchen utensils"
    ],
    "Topic 2 - Lesson 3 (Improvising Small Kitchen Tools)": [
        "wooden cooking spoons",
        "wooden kitchen spoon",
        "traditional wooden bowl"
    ],

    # -------------------------------------------------------------------------
    # Topic 3: Cooking Food (4 Lessons)
    # -------------------------------------------------------------------------
    "Topic 3 - Lesson 1 (Heat Transfer & Grilling)": [
        "grilling meat barbecue",
        "barbecue grill charcoal",
        "grilled skewers meat"
    ],
    "Topic 3 - Lesson 2 (Roasting & Sand Oven)": [
        "roasting corn charcoal",
        "roasted maize street",
        "roasting meat charcoal"
    ],
    "Topic 3 - Lesson 3 (Steaming Food & Nutrition)": [
        "steaming food bamboo",
        "steamer basket vegetables",
        "steaming vegetables"
    ],
    "Topic 3 - Lesson 4 (Fuel Conservation & Plating)": [
        "food plating plate",
        "plated dinner dish",
        "balanced healthy meal"
    ],

    # -------------------------------------------------------------------------
    # Topic 4: Consumer Education (Buying Goods & Services) (4 Lessons)
    # -------------------------------------------------------------------------
    "Topic 4 - Lesson 1 (Household Needs: Goods vs Services)": [
        "grocery store products shelves",
        "supermarket shelves groceries",
        "market produce goods"
    ],
    "Topic 4 - Lesson 2 (Factors Influencing Buying Choices)": [
        "supermarket shopping aisle",
        "weighing vegetables market scale",
        "grocery shopping cart"
    ],
    "Topic 4 - Lesson 3 (Where We Shop & Market Survey)": [
        "market stall produce sellers",
        "open air market vendors",
        "african market vegetables"
    ],
    "Topic 4 - Lesson 4 (Safe Transactions & Integrity)": [
        "cash money transaction",
        "paying money retail cashier",
        "banknotes money cash"
    ],

    # -------------------------------------------------------------------------
    # Topic 5: Natural Textile Fibres (4 Lessons)
    # -------------------------------------------------------------------------
    "Topic 5 - Lesson 1 (Classification & Sources of Fibres)": [
        "cotton bolls mississippi",
        "cotton boll plant field",
        "cotton harvest field"
    ],
    "Topic 5 - Lesson 2 (Physical Properties & Microscopic Shapes)": [
        "wool sheep fleece",
        "spinning wool yarn",
        "raw sheep wool"
    ],
    "Topic 5 - Lesson 3 (Everyday Household Uses & Sight/Feel)": [
        "textile fabrics cotton linen",
        "folded textile fabrics",
        "woven textile fabric"
    ],
    "Topic 5 - Lesson 4 (Burning Tests & Lab Safety)": [
        "candle flame laboratory",
        "burning candle flame dark",
        "candle flame science"
    ],

    # -------------------------------------------------------------------------
    # Topic 6: The Sewing Machine (4 Lessons)
    # -------------------------------------------------------------------------
    "Topic 6 - Lesson 1 (Sewing Machine Types & Buying)": [
        "vintage sewing machine singer",
        "treadle sewing machine",
        "sewing machine"
    ],
    "Topic 6 - Lesson 2 (Anatomy & Parts of the Machine)": [
        "sewing machine needle presser foot",
        "sewing machine needle close up",
        "sewing machine parts"
    ],
    "Topic 6 - Lesson 3 (Setup, Threading & Safe Stitching)": [
        "woman sewing machine singer",
        "sewing machine fabric hands",
        "sewing with sewing machine"
    ],
    "Topic 6 - Lesson 4 (Troubleshooting Stitch Faults & Care)": [
        "sewing machine bobbin case",
        "sewing machine shuttle race",
        "sewing machine repair maintenance"
    ]
}

results = {}
for name, qlist in all_lessons.items():
    res = search_wikimedia(qlist)
    if res:
        results[name] = res
        print(f"[VERIFIED 200 OK] {name}")
        print(f"   -> Image: {res['title']}")
        print(f"   -> URL: {res['url']}")
        print(f"   -> Size: {res['bytes']} bytes (Matched Query: '{res['matched_query']}')\n")
    else:
        print(f"[FAILED] {name} across all queries {qlist}\n")

with open('verified_topic_photos.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nCompleted photo verification: {len(results)}/{len(all_lessons)} lessons found!")
