import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_indented_lines(s):
    if not isinstance(s, str):
        return s
    lines = s.split('\n')
    cleaned = []
    in_code = False
    for l in lines:
        if l.strip().startswith('```'):
            in_code = not in_code
            cleaned.append(l)
            continue
        if not in_code:
            # Strip accidental 4-space indents on non-list items
            l = re.sub(r'^[ \t]{4,}(?![*\-\d]\s)', '', l)
        cleaned.append(l)
    return '\n'.join(cleaned)

def clean_obj(obj):
    if isinstance(obj, str):
        return clean_indented_lines(obj)
    if isinstance(obj, dict):
        return {k: clean_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_obj(x) for x in obj]
    return obj

fixed = 0
for b in LessonBlock.objects.all():
    if b.content:
        new_c = clean_obj(b.content)
        if new_c != b.content:
            b.content = new_c
            b.save(update_fields=['content'])
            fixed += 1

print(f"Fixed accidental indentation across {fixed} blocks in DB.")
