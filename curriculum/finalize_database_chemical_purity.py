import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_entire_field(s):
    if not isinstance(s, str):
        return s

    # 1. Strip ASCII 13 and non-printable control characters
    s = s.replace(chr(13), '')
    s = ''.join(c for c in s if ord(c) >= 32 or ord(c) in (9, 10))

    # 2. Convert all ightarrow variations to pure KaTeX \xrightarrow / \rightarrow
    s = s.replace(' ightarrow{', r' \xrightarrow{')
    s = s.replace('\nightarrow{', r'\n\xrightarrow{')
    s = s.replace('}ightarrow{', r'}\xrightarrow{')
    s = s.replace(')ightarrow{', r')\xrightarrow{')
    s = s.replace(' ightarrow ', r' \rightarrow ')
    s = s.replace(' ightarrow\n', r' \rightarrow\n')
    s = s.replace('\nightarrow ', r'\n\rightarrow ')
    s = s.replace('}ightarrow', r'}\rightarrow')
    s = s.replace(')ightarrow', r')\rightarrow')
    s = s.replace('ightarrow', r'\rightarrow')

    # 3. Convert all custom reaction conditions to standard KaTeX \xrightarrow
    s = s.replace(r'\rightarrow{\text{water}}', r'\xrightarrow{\text{water}}')
    s = s.replace(r'\rightarrow{\Delta}', r'\xrightarrow{\Delta}')
    s = s.replace(r'\rightarrow{\text{light}}', r'\xrightarrow{\text{light}}')
    s = s.replace(r'\rightarrow{\text{heat}}', r'\xrightarrow{\text{heat}}')
    s = s.replace(r'\rightarrow{\text{boiling}}', r'\xrightarrow{\text{boiling}}')
    s = s.replace(r'\rightarrow{\text{MnO}_2}', r'\xrightarrow{\text{MnO}_2}')
    s = s.replace(r'\rightarrow{900^\circ\text{C}}', r'\xrightarrow{900^\circ\text{C}}')
    s = s.replace(r'\rightarrow{1400^\circ\text{C}}', r'\xrightarrow{1400^\circ\text{C}}')
    s = s.replace(r'\rightarrow{< 45^\circ\text{C}}', r'\xrightarrow{< 45^\circ\text{C}}')
    s = s.replace(r'\rightarrow[\text{Pt-Rh Catalyst}]{900^\circ\text{C}}', r'\xrightarrow[\text{Pt-Rh Catalyst}]{900^\circ\text{C}}')

    # 4. Clean up any remaining \xr
    s = s.replace(r'\xr', '')

    # 5. Fix state subscripts
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def clean_data_structure(obj):
    if isinstance(obj, str):
        return clean_entire_field(obj)
    if isinstance(obj, dict):
        return {k: clean_data_structure(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_data_structure(x) for x in obj]
    return obj

updated = 0
for b in LessonBlock.objects.all():
    modified = False
    update_fields = []
    
    if b.title:
        nt = clean_entire_field(b.title)
        if nt != b.title:
            b.title = nt
            modified = True
            update_fields.append('title')

    if b.page_title:
        npt = clean_entire_field(b.page_title)
        if npt != b.page_title:
            b.page_title = npt
            modified = True
            update_fields.append('page_title')

    if b.content:
        nc = clean_data_structure(b.content)
        if nc != b.content:
            b.content = nc
            modified = True
            update_fields.append('content')

    if modified:
        b.save(update_fields=update_fields)
        updated += 1

print(f"Final Chemical Purity Pass complete: Successfully cleaned and saved {updated} blocks.")
