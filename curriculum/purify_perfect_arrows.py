import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_arrow_text(s):
    if not isinstance(s, str):
        return s

    # 1. Filter out all ASCII control characters (< 32) except \n (10) and \t (9)
    s = ''.join(c for c in s if ord(c) >= 32 or ord(c) in (9, 10))

    # 2. Fix \r\rightarrow or \xr\rightarrow or \rightarrow with braces -> \xrightarrow{...}
    s = re.sub(r'\\r\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\xr\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\rightarrow\[([^\]]+)\]\{([^}]+)\}', lambda m: r'\xrightarrow[' + m.group(1) + ']{' + m.group(2) + '}', s)
    s = re.sub(r'(?<![a-zA-Z\\])ightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)

    # 3. Fix bare \r\rightarrow or \xr\rightarrow -> \rightarrow
    s = re.sub(r'\\r\\rightarrow\b', r'\rightarrow', s)
    s = re.sub(r'\\xr\\rightarrow\b', r'\rightarrow', s)
    s = re.sub(r'(?<![a-zA-Z\\])ightarrow\b', r'\rightarrow', s)

    # 4. Clean up any trailing isolated \r or \xr
    s = re.sub(r'\\xr\b', '', s)
    s = re.sub(r'\\r\b', '', s)

    # 5. Fix state subscripts
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def clean_obj(obj):
    if isinstance(obj, str):
        return clean_arrow_text(obj)
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
        nt = clean_arrow_text(b.title)
        if nt != b.title:
            b.title = nt
            modified = True
            update_fields.append('title')

    if b.page_title:
        npt = clean_arrow_text(b.page_title)
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

print(f"Purification finished: Successfully updated {fixed} blocks across all subjects.")
