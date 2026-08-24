import sys
import os
import re
from pprint import pformat
import importlib.util

from curriculum.bs_verified_images import VERIFIED_IMAGES

class MockModule:
    def __getattr__(self, name):
        if name.startswith('SVG_'):
            return f"__MAGIC_{name}__"
        raise AttributeError(name)

sys.modules['curriculum.ingest_form4_business_studies_topic12_svgs'] = MockModule()
sys.modules['curriculum.ingest_form4_business_studies_topic13_svgs'] = MockModule()
sys.modules['curriculum.ingest_form4_business_studies_topic14_svgs'] = MockModule()

def load_module(filepath, module_name):
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def fix_bullets(text):
    if '•' not in text:
        return text
    parts = text.split('•')
    out = []
    if parts[0].strip():
        out.append(parts[0].strip())
    for part in parts[1:]:
        part = part.strip()
        if not part: continue
        colon_idx = part.find(':')
        if colon_idx != -1 and colon_idx < 40:
            key = part[:colon_idx].strip()
            if not key.startswith('**'):
                key = f"**{key}**"
            val = part[colon_idx+1:].strip()
            out.append(f"- {key}: {val}")
        else:
            out.append(f"- {part}")
    return "\n".join(out).replace('\n\n', '\n')

def process_topic(filepath, topic_name, images_mapping, unit_var_name):
    mod = load_module(filepath, topic_name)
    
    lesson_vars = [name for name in dir(mod) if name.startswith('LESSON_') and name.endswith('_DATA')]
    lesson_vars.sort(key=lambda x: int(x.split('_')[1]))
    
    out_lines = []
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract headers
    import_end = content.find('\n# Verified Wikimedia')
    if import_end == -1:
        import_end = content.find('IMG_')
    if import_end == -1:
        import_end = content.find('\nLESSON_1_DATA')
    
    out_lines.append(content[:import_end].strip() + '\n\n')
    
    for l_var in lesson_vars:
        lesson_data = getattr(mod, l_var)
        lesson_idx = lesson_data['unit_order']
        
        # 1. Add image
        if lesson_idx in images_mapping:
            img_key = images_mapping[lesson_idx]
            img = VERIFIED_IMAGES[img_key]
            
            photo_block = {
                "block_type": "suggested_image",
                "component_type": "photo_view",
                "title": "Real-World Context",
                "content": {
                    "url": img['url'],
                    "text": img['description'],
                    "author": img['author'],
                    "licensing": img['licensing'],
                    "commons_page_url": img['commons_page_url']
                }
            }
            
            for page in lesson_data['pages']:
                if page['page_number'] == 1:
                    if len(page['blocks']) == 0 or page['blocks'][0].get('component_type') != 'photo_view':
                        page['blocks'].insert(0, photo_block)
        
        # 2. Process blocks
        for page in lesson_data['pages']:
            for block in page['blocks']:
                c_type = block.get('component_type', '')
                b_type = block.get('block_type', '')
                
                # Semantic upgrades
                if c_type == 'concept_card' or c_type == 'text':
                    title = block.get('title', '').lower()
                    text = block.get('content', {}).get('text', '').lower()
                    
                    if any(x in title for x in ['watch out', 'common mistake', 'error']) or any(x in text for x in ['watch out', 'common mistake']):
                        block['component_type'] = 'common_mistake'
                    elif any(x in title for x in ['memory tip', 'remember', 'mnemonic']):
                        block['component_type'] = 'memory_tip'
                    elif any(x in title for x in ['key point', 'key takeaway', 'critical']) or 'key takeaway' in text:
                        block['component_type'] = 'key_takeaway'
                    elif 'important' in title or 'main principle' in title:
                        block['component_type'] = 'callout'
                    elif 'summary' in title:
                        block['component_type'] = 'summary'
                    elif c_type == 'text':
                        # generic text to concept_card
                        block['component_type'] = 'concept_card'
                
                # Fix bullets
                if 'content' in block and 'text' in block['content']:
                    block['content']['text'] = fix_bullets(block['content']['text'])
                
                # Upgrade learning_goal
                if block.get('component_type') == 'learning_goal' and 'text' in block.get('content', {}):
                    txt = block['content']['text']
                    txt = re.sub(r'(?i)By the end of this lesson,? you should be able to ', '', txt)
                    # split on ', and ' or ' and ' or ', '
                    txt = txt.replace(', and ', ', ').replace(' and ', ', ')
                    goals = [g.strip().capitalize() for g in txt.split(', ') if g.strip()]
                    block['content']['goals'] = goals
                    del block['content']['text']
                
                # Upgrade worked_example
                if block.get('component_type') == 'worked_example' and 'text' in block.get('content', {}):
                    txt = block['content']['text']
                    if '1. ' in txt and '2. ' in txt:
                        parts = re.split(r'\n?\d+\.\s+', txt)
                        intro = parts[0].strip()
                        steps = [p.strip() for p in parts[1:] if p.strip()]
                        if intro:
                            block['content']['intro'] = intro
                        block['content']['steps'] = steps
                        del block['content']['text']
        
        # Serialize
        dict_str = pformat(lesson_data, width=120, sort_dicts=False)
        dict_str = dict_str.replace("'__MAGIC_", "")
        dict_str = dict_str.replace("__'", "")
        
        out_lines.append(f"{l_var} = {dict_str}\n\n")
    
    out_lines.append(f"{unit_var_name} = [{', '.join(lesson_vars)}]\n")
    
    with open(filepath, 'w') as f:
        f.write("".join(out_lines))
    print(f"Processed {filepath}")

# Topic 12
process_topic('curriculum/topic12_data.py', 'topic12', {
    1: 'accountant_desk',
    2: 'analyzing_financial_data',
    3: 'ledger_book'
}, 'TOPIC12_UNITS')

# Topic 13
process_topic('curriculum/topic13_data.py', 'topic13', {
    1: 'bank_tellers',
    2: 'atm_machine',
    3: 'accountant_desk',
    4: 'analyzing_financial_data'
}, 'TOPIC13_UNITS')

# Topic 14
process_topic('curriculum/topic14_data.py', 'topic14', {
    1: 'analyzing_financial_data',
    2: 'wangige_market',
    3: 'jua_kali_fabricator',
    4: 'accountant_desk',
    5: 'millinery_ledger'
}, 'TOPIC14_UNITS')

