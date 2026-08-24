import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def master_clean_string(s):
    if not isinstance(s, str):
        return s

    # 1. Strip all ASCII control characters except \n and \t
    # ASCII 13 (\r), ASCII 7 (\a / bell), ASCII 8 (\b / backspace), etc.
    s = s.replace('\x08eta', r'\beta')
    s = s.replace('\x08ar', r'\bar')
    s = s.replace('\x07lpha', r'\alpha')
    s = re.sub(r'[\x00-\x08\x0b\x0c\x0d\x0e-\x1f\x7f]', '', s)

    # 2. Fix ightarrow (where \r was stripped earlier leaving ightarrow)
    # Convert ightarrow{condition} or \rightarrow{condition} -> \xrightarrow{condition}
    s = re.sub(r'\\?x?r?ightarrow\{([^}]+)\}', lambda m: r'\xrightarrow{' + m.group(1) + '}', s)
    s = re.sub(r'\\?x?r?ightarrow\[([^\]]+)\]\{([^}]+)\}', lambda m: r'\xrightarrow[' + m.group(1) + ']{' + m.group(2) + '}', s)
    
    # 3. Convert bare ightarrow or \xr\rightarrow -> \rightarrow
    s = re.sub(r'\\(?:xr\\)*xr\\rightarrow', r'\rightarrow', s)
    s = re.sub(r'\\?x?r?ightarrow', r'\rightarrow', s)
    s = re.sub(r'\\xr\b', '', s)

    # 4. Fix state subscripts (e.g. *{(s)} or \_{(aq)})
    s = re.sub(r'(\\\w+|\})\s*\*\s*\{(\([a-zA-Z]+\))\s*\}', r'\1_{\2}', s)
    s = re.sub(r'\*\s*\{(\([a-zA-Z]+\))\s*\}', r'_{\1}', s)
    s = re.sub(r'\\\_\{', r'_{', s)
    s = re.sub(r'\\\^\{', r'^{', s)
    s = re.sub(r'\\\_([a-zA-Z0-9])', r'_\1', s)
    s = re.sub(r'\\\^([a-zA-Z0-9])', r'^\1', s)

    # 5. Fix isolated operator dollars inside chemical equations
    s = re.sub(r'\$(?:\\rightarrow|\\rightleftharpoons|\\leftarrow|\\Delta|\\pm|\\times|\\approx)\$', lambda m: m.group(0)[1:-1], s)
    s = re.sub(r'\$\s*\\Delta\s*\$\s*H', r'\\Delta H', s)

    # 6. Fix nested or double $$
    s = re.sub(r'\$\$\s*\$\$', '$$', s)

    return s

def recursive_clean_data(obj):
    if isinstance(obj, str):
        return master_clean_string(obj)
    if isinstance(obj, dict):
        return {k: recursive_clean_data(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [recursive_clean_data(x) for x in obj]
    return obj

count = 0
for b in LessonBlock.objects.all():
    modified = False
    update_fields = []
    
    if b.title:
        new_title = master_clean_string(b.title)
        if new_title != b.title:
            b.title = new_title
            modified = True
            update_fields.append('title')

    if b.page_title:
        new_page_title = master_clean_string(b.page_title)
        if new_page_title != b.page_title:
            b.page_title = new_page_title
            modified = True
            update_fields.append('page_title')

    if b.content:
        new_content = recursive_clean_data(b.content)
        if new_content != b.content:
            b.content = new_content
            modified = True
            update_fields.append('content')

    if modified:
        b.save(update_fields=update_fields)
        count += 1

print(f"Master cleaned {count} blocks across entire database.")
