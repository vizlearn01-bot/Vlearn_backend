import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_database_equation_string(s):
    if not isinstance(s, str):
        return s

    # 1. Remove all \r carriage returns
    s = s.replace('\r', '')

    # 2. Fix \xr\xr\rightarrow or \xr\rightarrow{condition} -> \xrightarrow{condition}
    s = re.sub(r'\\(?:xr\\)*xr\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\(?:xr\\)*rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\rightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\bightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)

    # 3. Fix bare corrupted arrows -> \rightarrow
    s = re.sub(r'\\(?:xr\\)*xr\\rightarrow\b', r'\rightarrow', s)
    s = re.sub(r'\\xr\b', '', s)
    s = re.sub(r'\bightarrow\b', r'\rightarrow', s)

    # 4. Fix state subscripts
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = s.replace(r'\_', '_').replace(r'\^', '^')

    return s

def clean_db_obj(obj):
    if isinstance(obj, str):
        return clean_database_equation_string(obj)
    if isinstance(obj, dict):
        return {k: clean_db_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_db_obj(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.filter(lesson__topic__subject__name='Chemistry'):
    if b.content:
        new_c = clean_db_obj(b.content)
        if new_c != b.content:
            b.content = new_c
            b.save(update_fields=['content'])
            fixed += 1

print(f"Cleaned {fixed} blocks in database.")
