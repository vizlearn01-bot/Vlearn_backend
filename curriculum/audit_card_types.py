import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Checking all learning_goal, common_misconception, definition_card, and summary blocks...")

target_types = ['learning_goal', 'common_misconception', 'definition_card', 'definition', 'summary', 'key_takeaway']
blocks = LessonBlock.objects.filter(block_type__in=target_types)

suspicious = []
for b in blocks:
    raw = json.dumps(b.content)
    # Check if there are $$...$$ wrapping English text or unclosed single $
    display_matches = re.findall(r'\$\$([^\$]+)\$\$', raw)
    for dm in display_matches:
        words = re.findall(r'[a-zA-Z]{3,}', dm)
        non_latex = [w for w in words if w.lower() not in ['frac', 'sqrt', 'times', 'text', 'mathrm', 'mathbf', 'approx', 'implies', 'propto', 'rightleftharpoons', 'rightarrow', 'quad', 'qquad', 'cdot', 'delta', 'rho', 'alpha', 'beta', 'theta', 'lambda', 'sigma', 'omega', 'over', 'left', 'right', 'circ', 'degree']]
        if len(non_latex) >= 2:
            suspicious.append((b, dm))

print(f"Total target blocks checked: {blocks.count()}")
print(f"Suspicious blocks remaining: {len(suspicious)}")
for b, dm in suspicious[:10]:
    print(f"Lesson {b.lesson_id} | Block {b.id} ({b.block_type}) | Title: {b.title}")
    print(f"   Snippet: {dm[:100]}")
