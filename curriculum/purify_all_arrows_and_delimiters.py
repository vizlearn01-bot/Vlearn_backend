import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def purify_string(s):
    if not isinstance(s, str):
        return s

    # 1. Strip raw carriage returns (\r / ASCII 13) completely
    s = s.replace('\r', '')
    
    # 2. Fix \xr\rightarrow or ightarrow (where \r became carriage return)
    # Convert arrow with condition: \rightarrow{water} or ightarrow{water} -> \xrightarrow{water}
    s = re.sub(r'\\?x?r?i?g?h?t?a?r?r?o?w\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\xrightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    
    # Convert bare corrupted arrows -> \rightarrow
    s = re.sub(r'\\xr[a-zA-Z\\]*', r'\rightarrow', s)
    s = re.sub(r'\\?ightarrow\b', r'\rightarrow', s)

    # 3. Fix state subscripts
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def purify_obj(obj):
    if isinstance(obj, str):
        return purify_string(obj)
    if isinstance(obj, dict):
        return {k: purify_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [purify_obj(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.filter(lesson__topic__subject__name='Chemistry'):
    if b.content:
        new_c = purify_obj(b.content)
        if new_c != b.content:
            b.content = new_c
            b.save(update_fields=['content'])
            fixed += 1

print(f"Purified {fixed} blocks across Chemistry corpus.")
