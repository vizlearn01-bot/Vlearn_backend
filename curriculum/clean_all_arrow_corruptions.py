import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_block_string(text):
    if not isinstance(text, str):
        return text

    # 1. Filter out all ASCII control characters (< 32) except \n (10) and \t (9)
    text = ''.join(c for c in text if ord(c) >= 32 or ord(c) in (9, 10))

    # 2. Fix isolated 'ightarrow' without altering 'xrightarrow'
    text = text.replace(' ightarrow{', r' \xrightarrow{')
    text = text.replace(' ightarrow ', r' \rightarrow ')
    text = text.replace('\nightarrow{', r'\n\xrightarrow{')
    text = text.replace('\nightarrow ', r'\n\rightarrow ')
    text = text.replace('^ightarrow', r'^\rightarrow')
    text = text.replace('{ightarrow}', r'{\rightarrow}')
    text = text.replace(' ightarrow\n', r' \rightarrow\n')
    
    # 3. Handle \rightarrow{condition} -> \xrightarrow{condition}
    text = text.replace(r'\xrightarrow', '__XARR__')
    text = text.replace(r'\rightarrow{', r'\xrightarrow{')
    text = text.replace(r'__XARR__', r'\xrightarrow')

    # 4. Clean up any remaining corrupted \xr\rightarrow
    text = text.replace(r'\xr\rightarrow', r'\xrightarrow')
    text = text.replace(r'\xr', '')

    # 5. Fix state subscripts
    text = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', text)
    text = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', text)
    text = text.replace(r'\_', '_').replace(r'\^', '^')

    return text

def recursive_clean_structure(obj):
    if isinstance(obj, str):
        return clean_block_string(obj)
    if isinstance(obj, dict):
        return {k: recursive_clean_structure(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [recursive_clean_structure(x) for x in obj]
    return obj

fixed_count = 0
for b in LessonBlock.objects.all():
    modified = False
    update_fields = []
    
    if b.title:
        new_title = clean_block_string(b.title)
        if new_title != b.title:
            b.title = new_title
            modified = True
            update_fields.append('title')

    if b.page_title:
        new_page_title = clean_block_string(b.page_title)
        if new_page_title != b.page_title:
            b.page_title = new_page_title
            modified = True
            update_fields.append('page_title')

    if b.content:
        new_content = recursive_clean_structure(b.content)
        if new_content != b.content:
            b.content = new_content
            modified = True
            update_fields.append('content')

    if modified:
        b.save(update_fields=update_fields)
        fixed_count += 1

print(f"Purified and finalized {fixed_count} blocks across entire curriculum database.")
