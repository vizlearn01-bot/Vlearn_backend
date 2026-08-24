import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def purify_field(s):
    if not isinstance(s, str):
        return s

    # 1. Strip ASCII 13 (carriage return) and control characters
    s = s.replace(chr(13), '')
    s = ''.join(c for c in s if ord(c) >= 32 or ord(c) in (9, 10))

    # 2. Fix corrupted arrows WITH conditions -> \xrightarrow{condition}
    # Use lambda to prevent re.sub from interpreting \x and \r as escape codes!
    s = re.sub(r'\\?x?r?ightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\?x?r?ightarrow\[([^\]]+)\]\{([^}]+)\}', lambda m: r'\xrightarrow[' + m.group(1) + ']{' + m.group(2) + '}', s)
    s = re.sub(r'\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)

    # 3. Fix bare corrupted arrows -> \rightarrow
    s = re.sub(r'\\r\\rightarrow', lambda m: r'\rightarrow', s)
    s = re.sub(r'\\xr\\rightarrow', lambda m: r'\rightarrow', s)
    s = re.sub(r'(?<![a-zA-Z\\])ightarrow', lambda m: r'\rightarrow', s)
    s = re.sub(r'\\xr\b', '', s)
    s = re.sub(r'\\r\b', '', s)

    # 4. Fix state subscripts
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def recursive_purify(obj):
    if isinstance(obj, str):
        return purify_field(obj)
    if isinstance(obj, dict):
        return {k: recursive_purify(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [recursive_purify(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.all():
    modified = False
    update_fields = []
    
    if b.title:
        nt = purify_field(b.title)
        if nt != b.title:
            b.title = nt
            modified = True
            update_fields.append('title')

    if b.page_title:
        npt = purify_field(b.page_title)
        if npt != b.page_title:
            b.page_title = npt
            modified = True
            update_fields.append('page_title')

    if b.content:
        nc = recursive_purify(b.content)
        if nc != b.content:
            b.content = nc
            modified = True
            update_fields.append('content')

    if modified:
        b.save(update_fields=update_fields)
        fixed += 1

print(f"Master purification pass complete: Successfully fixed {fixed} blocks across all subjects.")
