import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

lessons = Lesson.objects.all()
leaks_found = 0

for les in lessons:
    for b in les.blocks.all():
        raw_text = ''
        if isinstance(b.content, dict):
            raw_text = b.content.get('text', '') or b.content.get('body', '') or json.dumps(b.content)
        elif isinstance(b.content, str):
            raw_text = b.content

        # Strip display math $$...$$ and inline math $...$
        stripped = re.sub(r'\$\$[\s\S]*?\$\$', '', raw_text)
        stripped = re.sub(r'\$[^\$\n]+?\$', '', stripped)
        
        # Check for LaTeX backslashes that are leaking
        naked = re.findall(r'\\(?:frac|sqrt|implies|propto|times|approx|circ|rightarrow|rightleftharpoons|rho|Delta)\b', stripped)
        if naked:
            leaks_found += 1
            print(f'Lesson {les.id} ({les.title}) | Page {b.page_number} | Block {b.id} | Leaking: {set(naked)}')
            for line in raw_text.split('\n'):
                if any(cmd in line for cmd in naked):
                    print(f'   > {line.strip()[:100]}')

print(f'TOTAL LEAKS FOUND ACROSS ENTIRE CURRICULUM: {leaks_found}')
