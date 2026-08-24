import os, sys, django, re, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

lessons = Lesson.objects.all()
updated_count = 0

for les in lessons:
    for b in les.blocks.all():
        if not isinstance(b.content, dict):
            continue
        
        modified = False
        
        # 1. Clean steps array if present
        if 'steps' in b.content and isinstance(b.content['steps'], list):
            new_steps = []
            for s in b.content['steps']:
                if isinstance(s, str):
                    lines = s.split('\n')
                    new_lines = []
                    for line in lines:
                        trimmed = line.strip()
                        if trimmed.startswith('$$') or (trimmed.startswith('$') and trimmed.endswith('$')):
                            new_lines.append(line)
                            continue
                        
                        has_math = bool(re.search(r'\\(?:frac|sqrt|implies|propto|times|approx|circ|rightarrow|rightleftharpoons)\b', trimmed))
                        is_prose = bool(re.match(r'^(?:For|If|When|Where|Note|Since|Then|According|Therefore|Thus|Hence|Step|Given|The|A|An|What|We|Identify|Convert|Determine|State|Substitute|Calculate|Solve|Scientific)\b', trimmed, re.I))
                        
                        if has_math and not is_prose and not trimmed.startswith('#') and not trimmed.startswith('```') and not trimmed.startswith('-'):
                            new_lines.append(f"$${trimmed}$$")
                            modified = True
                        else:
                            new_lines.append(line)
                    new_steps.append('\n'.join(new_lines))
                else:
                    new_steps.append(s)
            b.content['steps'] = new_steps

        # 2. Clean text fields
        for key in ['text', 'content', 'explanation', 'body', 'definition', 'problem', 'question']:
            if key in b.content and isinstance(b.content[key], str):
                val = b.content[key]
                lines = val.split('\n')
                new_lines = []
                for line in lines:
                    trimmed = line.strip()
                    if trimmed.startswith('$$') or (trimmed.startswith('$') and trimmed.endswith('$')):
                        new_lines.append(line)
                        continue
                    
                    has_math = bool(re.search(r'\\(?:frac|sqrt|implies|propto|rightleftharpoons)\b', trimmed))
                    is_prose = bool(re.match(r'^(?:For|If|When|Where|Note|Since|Then|According|Therefore|Thus|Hence|Step|Given|The|A|An|What|We|Identify|Convert|Determine|State|Substitute|Calculate|Solve|Scientific|Does|Why|Which|How)\b', trimmed, re.I))
                    
                    if has_math and not is_prose and not trimmed.startswith('#') and not trimmed.startswith('```') and not trimmed.startswith('-'):
                        new_lines.append(f"$${trimmed}$$")
                        modified = True
                    else:
                        new_lines.append(line)
                
                b.content[key] = '\n'.join(new_lines)
        
        if modified:
            b.save()
            updated_count += 1
            print(f"Updated Lesson {les.id} ({les.title}) Block {b.id}")

print(f"Cleaned {updated_count} blocks across curriculum!")
