import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def sanitize_db_string(s):
    if not isinstance(s, str):
        return s
    
    # 1. Convert ightarrow / \rightarrow{condition} -> \xrightarrow{condition}
    s = re.sub(r'\\?ightarrow\{([^}]+)\}', lambda m: rf"\xrightarrow{{{m.group(1)}}}", s)
    s = re.sub(r'\\rightarrow\{([^}]+)\}', lambda m: rf"\xrightarrow{{{m.group(1)}}}", s)
    s = re.sub(r'\\rightarrow\[([^\]]+)\]\{([^}]+)\}', lambda m: rf"\xrightarrow[{m.group(1)}]{{{m.group(2)}}}", s)
    s = re.sub(r'\\xr[a-zA-Z\\]*', r'\rightarrow', s)

    # 2. Convert raw math outside $$ / $
    # Fix broken state subscripts like *{(s)} or \_{(s)}
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def sanitize_obj(obj):
    if isinstance(obj, str):
        return sanitize_db_string(obj)
    if isinstance(obj, dict):
        return {k: sanitize_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [sanitize_obj(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.filter(lesson__topic__subject__name='Chemistry'):
    if b.content:
        new_c = sanitize_obj(b.content)
        if new_c != b.content:
            b.content = new_c
            b.save(update_fields=['content'])
            fixed += 1

print(f"Sanitized {fixed} blocks in database.")
