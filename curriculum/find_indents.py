import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

print("Searching for blocks with 4-space indented non-code lines...")
indented_blocks = []

for b in LessonBlock.objects.all():
    s = str(b.content or '')
    lines = s.split('\n')
    found_lines = []
    in_fenced_code = False
    for l in lines:
        if l.strip().startswith('```'):
            in_fenced_code = not in_fenced_code
            continue
        if not in_fenced_code and re.match(r'^[ ]{4,}(?![*\-\d]\s)[a-zA-Z\$\(\*\_]', l):
            found_lines.append(l.strip())
            
    if found_lines:
        indented_blocks.append((b.id, b.lesson.id if b.lesson else None, b.lesson.title if b.lesson else '', found_lines[:3]))

print(f"Total blocks with accidental 4-space code indents: {len(indented_blocks)}")
for ib in indented_blocks[:15]:
    print(f"Block [{ib[0]}] in Lesson [{ib[1]}] \"{ib[2]}\":")
    print("   Indented text:", ib[3])
    print()
