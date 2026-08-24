import os, sys, django, re, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson

chem_lessons = Lesson.objects.filter(topic__subject__name__icontains='Chemistry')

for les in chem_lessons:
    for b in les.blocks.all():
        if not isinstance(b.content, dict):
            continue
        
        modified = False
        for key in ['text', 'content', 'explanation', 'body', 'definition']:
            if key in b.content and isinstance(b.content[key], str):
                val = b.content[key]
                lines = val.split('\n')
                new_lines = []
                for line in lines:
                    trimmed = line.strip()
                    # If this line is already in $$...$$ or $...$, leave it
                    if trimmed.startswith('$$') or (trimmed.startswith('$') and trimmed.endswith('$')):
                        new_lines.append(line)
                        continue
                    
                    # If the line has LaTeX math commands and is not a prose sentence
                    has_cmd = bool(re.search(r'\\(?:propto|frac|sqrt|implies|rightleftharpoons|rightarrow\{)\b', trimmed))
                    is_prose = bool(re.match(r'^(?:For|If|When|Where|Note|Since|Then|According|Therefore|Thus|Hence|Step|Given|The|A|An)\b', trimmed, re.I))
                    
                    if has_cmd and not is_prose and not trimmed.startswith('#') and not trimmed.startswith('```'):
                        new_lines.append(f"$${trimmed}$$")
                        modified = True
                    else:
                        new_lines.append(line)
                
                if modified:
                    b.content[key] = '\n'.join(new_lines)
        
        if modified:
            b.save()
            print(f"Cleaned Lesson {les.id} Block {b.id}")

print("Done cleaning naked math in Chemistry blocks!")
