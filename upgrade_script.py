import re
import os
import json
from curriculum.bs_verified_images import VERIFIED_IMAGES

def get_image_block(img_key, title):
    img = VERIFIED_IMAGES[img_key]
    block = f"""{{
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "{title}",
                    "content": {{
                        "url": "{img['url']}",
                        "text": "{img['description']}",
                        "author": "{img['author']}",
                        "licensing": "{img['licensing']}",
                        "commons_page_url": "{img['commons_page_url']}"
                    }}
                }},"""
    return block

def fix_bullets(text):
    if '•' not in text:
        return text
    # Replace single line bullets
    parts = text.split('•')
    # If the text doesn't start with •, the first part is intro text
    out = []
    if parts[0].strip():
        out.append(parts[0].strip())
    for part in parts[1:]:
        part = part.strip()
        if not part: continue
        # Find first colon to bold
        colon_idx = part.find(':')
        if colon_idx != -1 and colon_idx < 40: # heuristically, if colon is soon, it's a key term
            key = part[:colon_idx].strip()
            # If it's already bolded, don't bold again
            if not key.startswith('**'):
                key = f"**{key}**"
            val = part[colon_idx+1:].strip()
            out.append(f"- {key}: {val}")
        else:
            out.append(f"- {part}")
    return "\\n".join(out).replace('\\n\\n', '\\n')

def upgrade_learning_goals(text):
    # Match text block inside learning goal
    pass

