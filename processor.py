import ast
import re
import importlib.util
import sys
import os

spec = importlib.util.spec_from_file_location("bs_verified_images", "curriculum/bs_verified_images.py")
bs_verified_images = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bs_verified_images)
VERIFIED_IMAGES = bs_verified_images.VERIFIED_IMAGES

IMAGE_MAPPING = {
    4: {
        0: 'nairobi_aerial',
        1: 'sgr_train',
        2: 'wangige_market',
        3: 'kenyan_currency',
        4: 'analyzing_financial_data'
    },
    5: {
        0: 'wangige_market',
        1: 'nairobi_vegetable',
        2: 'kibera_slum'
    },
    6: {
        0: 'nairobi_aerial',
        1: 'kibera_slum',
        2: 'nairobi_vegetable',
        3: 'mombasa_container_ship',
        4: 'analyzing_financial_data'
    },
    7: {
        0: 'mombasa_container_ship',
        1: 'mombasa_port',
        2: 'mombasa_container_ship',
        3: 'analyzing_financial_data',
        4: 'kenyan_currency'
    },
    8: {
        0: 'eac_flags',
        1: 'eac_community',
        2: 'mombasa_container_ship'
    }
}

def process_block(block):
    if not isinstance(block, dict): return block
    
    # Check for text replacement
    btype = block.get('block_type')
    ctype = block.get('component_type')
    
    if ctype == 'concept_card' and 'content' in block and isinstance(block['content'], dict) and 'text' in block['content']:
        block['content']['text'] = block['content']['text'].replace('•', '- ')
        
    title_lower = block.get('title', '').lower()
    
    if btype == 'text' and ctype == 'learning_goal' and 'content' in block and isinstance(block['content'], dict):
        text = block['content'].get('text', '')
        if text:
            goals = [g.strip().lstrip('-').lstrip('•').strip() for g in text.split('\n') if g.strip()]
            block['content'] = {'goals': [g for g in goals if g]}
        
    elif btype == 'text' and ctype == 'definition_card' and 'content' in block and isinstance(block['content'], dict):
        text = block['content'].get('text', '')
        if text:
            if ':' in text:
                term, defi = text.split(':', 1)
            elif '-' in text:
                term, defi = text.split('-', 1)
            else:
                term = block.get('title', 'Term')
                defi = text
            block['content'] = {'term': term.strip(), 'definition': defi.strip()}
        
    elif btype == 'text' and ctype == 'worked_example' and 'content' in block and isinstance(block['content'], dict):
        text = block['content'].get('text', '')
        if text:
            lines = text.split('\n')
            steps = []
            for line in lines:
                line = line.strip()
                if line: steps.append(line)
            block['content'] = {'steps': steps}
        
    # Upgrade component type based on title
    if 'watch out' in title_lower or 'common mistake' in title_lower:
        block['component_type'] = 'common_mistake'
    elif 'exam tip' in title_lower or 'key takeaway' in title_lower:
        block['component_type'] = 'key_takeaway'
    elif 'memory tip' in title_lower or 'mnemonic' in title_lower:
        block['component_type'] = 'memory_tip'
    elif 'rule' in title_lower or 'principle' in title_lower:
        if ctype == 'text':
            block['component_type'] = 'callout'
            
    return block

def process_topic(topic_id):
    file_path = f"curriculum/topic{topic_id}_data.py"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    spec = importlib.util.spec_from_file_location(f"topic{topic_id}", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    units = getattr(module, f"TOPIC{topic_id}_UNITS")
    
    for idx, unit in enumerate(units):
        # unit is a dict with 'title' and 'lessons' or just a list of pages?
        # Let's check structure. Wait, TOPIC4_UNITS = [LESSON_1_DATA, ...]
        # And LESSON_1_DATA is a list of pages? Let's check.
        if isinstance(unit, dict) and "pages" in unit:
            pages = unit["pages"]
        elif isinstance(unit, list):
            pages = unit
        else:
            pages = []
            
        for page in pages:
            if not isinstance(page, dict):
                continue
            blocks = page.get("blocks", [])
            new_blocks = []
            
            if page.get("page_number") == 1:
                img_key = IMAGE_MAPPING[topic_id][idx]
                if img_key not in VERIFIED_IMAGES:
                    # fallback to string mapping since there's a missing image name
                    print(f"Warning: {img_key} not found in verified images")
                    continue
                img_data = VERIFIED_IMAGES[img_key]
                img_block = {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": f"Real-world Context: {img_key.replace('_', ' ').title()}",
                    "content": {
                        "url": img_data["url"],
                        "text": img_data.get("description", "Image"),
                        "author": img_data.get("author", "Wikimedia"),
                        "licensing": img_data.get("licensing", "CC BY-SA"),
                        "commons_page_url": img_data.get("commons_page_url", "")
                    }
                }
                new_blocks.append(img_block)
                
            for b in blocks:
                new_blocks.append(process_block(b))
                
            page["blocks"] = new_blocks

    import pprint
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f'TOPIC{topic_id}_UNITS = \\\n')
        f.write(pprint.pformat(units, width=120, sort_dicts=False))
        f.write('\n')
        
    print(f"Topic {topic_id} processed.")

for t in range(4, 9):
    try:
        process_topic(t)
    except Exception as e:
        import traceback
        traceback.print_exc()

