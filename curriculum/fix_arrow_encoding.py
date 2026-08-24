import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_arrow_string(s):
    if not isinstance(s, str):
        return s

    # 1. Replace ASCII 13 carriage returns or \r before ightarrow
    s = s.replace('\r', '')
    
    # 2. Fix \xr\rightarrow{condition} or ightarrow{condition} -> \xrightarrow{condition}
    s = re.sub(r'\\xr[a-zA-Z\\]*\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'(?:\\rightarrow|\\?ightarrow)\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'(?:\\rightarrow|\\?ightarrow)\[([^\]]+)\]\{([^}]+)\}', lambda m: r'\xrightarrow[' + m.group(1) + ']{' + m.group(2) + '}', s)
    
    # 3. Fix remaining \xr or ightarrow -> \rightarrow
    s = re.sub(r'\\xr[a-zA-Z\\]*', r'\rightarrow', s)
    s = re.sub(r'(?:\\rightarrow|\\?ightarrow)', r'\rightarrow', s)

    # 4. Fix state subscripts
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def clean_obj(obj):
    if isinstance(obj, str):
        return clean_arrow_string(obj)
    if isinstance(obj, dict):
        return {k: clean_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_obj(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.filter(lesson__topic__subject__name='Chemistry'):
    if b.content:
        new_c = clean_obj(b.content)
        if new_c != b.content:
            b.content = new_c
            b.save(update_fields=['content'])
            fixed += 1

print(f"Fixed {fixed} blocks with corrupted arrow encodings in database.")
