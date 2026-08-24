import os, sys, django, re, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson

chem_lessons = Lesson.objects.filter(topic__subject__name__icontains='Chemistry')
print(f"Total Chemistry Lessons: {chem_lessons.count()}")

unwrapped_blocks = []
for les in chem_lessons:
    for b in les.blocks.all():
        raw_text = ''
        if isinstance(b.content, dict):
            raw_text = b.content.get('text', '') or b.content.get('body', '') or json.dumps(b.content)
        elif isinstance(b.content, str):
            raw_text = b.content

        # Strip all $$...$$ and $...$
        stripped = re.sub(r'\$\$[\s\S]*?\$\$', '', raw_text)
        stripped = re.sub(r'\$[^\$\n]+?\$', '', stripped)
        
        naked_commands = re.findall(r'\\(?:propto|frac|sqrt|implies|quad|rightleftharpoons|rightarrow\{|times|approx|Delta)\b', stripped)
        if naked_commands:
            unwrapped_blocks.append((les.id, les.title, b.id, b.page_number, set(naked_commands), raw_text))

print(f"Total blocks with naked math commands: {len(unwrapped_blocks)}")
for les_id, title, bid, page, cmds, text in unwrapped_blocks[:10]:
    print(f"Lesson {les_id} ({title}) | Block {bid} (Card {page}) | Commands: {cmds}")
