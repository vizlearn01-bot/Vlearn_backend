import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_arrow(s):
    if not isinstance(s, str):
        return s

    # 1. Strip all ASCII control characters (< 32) except \n (10) and \t (9)
    s = ''.join(c for c in s if ord(c) >= 32 or ord(c) in (9, 10))

    # 2. Fix ightarrow with condition -> \xrightarrow{condition}
    s = s.replace(' ightarrow{', r' \xrightarrow{')
    s = s.replace('\nightarrow{', r'\n\xrightarrow{')
    s = s.replace(')ightarrow{', r')\xrightarrow{')
    s = s.replace('}ightarrow{', r'}\xrightarrow{')
    s = s.replace('ightarrow{', r'\xrightarrow{')

    # 3. Fix bare ightarrow -> \rightarrow
    s = s.replace(' ightarrow ', r' \rightarrow ')
    s = s.replace(' ightarrow\n', r' \rightarrow\n')
    s = s.replace('\nightarrow ', r'\n\rightarrow ')
    s = s.replace(')ightarrow', r')\rightarrow')
    s = s.replace('}ightarrow', r'}\rightarrow')
    s = s.replace('ightarrow', r'\rightarrow')

    # 4. Handle \rightarrow{condition} -> \xrightarrow{condition}
    s = s.replace(r'\xrightarrow', '__XARR__')
    s = s.replace(r'\rightarrow{', r'\xrightarrow{')
    s = s.replace('__XARR__', r'\xrightarrow')

    # 5. Clean up any remaining \xr
    s = s.replace(r'\xr', '')

    return s

def clean_obj(obj):
    if isinstance(obj, str):
        return clean_arrow(obj)
    if isinstance(obj, dict):
        return {k: clean_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_obj(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.all():
    modified = False
    update_fields = []
    
    if b.title:
        nt = clean_arrow(b.title)
        if nt != b.title:
            b.title = nt
            modified = True
            update_fields.append('title')

    if b.page_title:
        npt = clean_arrow(b.page_title)
        if npt != b.page_title:
            b.page_title = npt
            modified = True
            update_fields.append('page_title')

    if b.content:
        nc = clean_obj(b.content)
        if nc != b.content:
            b.content = nc
            modified = True
            update_fields.append('content')

    if modified:
        b.save(update_fields=update_fields)
        fixed += 1

print(f"Final cleanup complete: Fixed {fixed} blocks across all subjects.")
