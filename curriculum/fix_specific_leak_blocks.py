import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Fixing remaining specific leak blocks...")

# 1. Block 14597 (Lesson 245) - stray $ in step_process
b = LessonBlock.objects.get(id=14597)
if isinstance(b.content, dict) and 'steps' in b.content:
    b.content['steps'] = [s.replace('$', '') if s.strip() == '$' else s for s in b.content['steps']]
    b.save()
    print("Fixed Block 14597")

# 2. Block 1734 (Lesson 67) - Reversible reactions
b = LessonBlock.objects.get(id=1734)
t = b.content.get('text', '')
t = t.replace(r'\rightleftharpoons', r'$\rightleftharpoons$')
b.content['text'] = t
b.save()
print("Fixed Block 1734")

# 3. Block 13619 (Lesson 214) - Longitude calculations
b = LessonBlock.objects.get(id=13619)
t = b.content.get('body', '')
t = re.sub(r'(?<!\$)\\(?:frac|circ)\{[^}]+\}(?:\{[^}]+\})?(?!\$)', lambda m: f"${m.group(0)}$", t)
t = re.sub(r'(?<!\$)\^\\circ(?!\$)', lambda m: '$^\\circ$', t)
b.content['body'] = t
b.save()
print("Fixed Block 13619")

# 4. Block 3335 (Lesson 80) - Redox reactions
b = LessonBlock.objects.get(id=3335)
t = b.content.get('text', '')
t = re.sub(r'(?<!\$)\\(?:text|rightarrow)\{[^}]+\}(?!\$)', lambda m: f"${m.group(0)}$", t)
b.content['text'] = t
b.save()
print("Fixed Block 3335")

# 5. Block 14038 (Lesson 232) - Trapezium rule formula
b = LessonBlock.objects.get(id=14038)
f = b.content.get('formula', '')
if not f.startswith('$$'):
    b.content['formula'] = f"$$\n{f}\n$$"
    b.save()
    print("Fixed Block 14038")

# 6. Block 14049 (Lesson 233) - Mid-ordinate rule formula
b = LessonBlock.objects.get(id=14049)
f = b.content.get('formula', '')
if not f.startswith('$$'):
    b.content['formula'] = f"$$\n{f}\n$$"
    b.save()
    print("Fixed Block 14049")

# 7. Block 1786 (Lesson 71) - Effect of pressure on equilibrium
b = LessonBlock.objects.get(id=1786)
t = b.content.get('text', '')
t = t.replace(r'\rightleftharpoons', r'$\rightleftharpoons$')
b.content['text'] = t
b.save()
print("Fixed Block 1786")

# 8. Block 5508 (Lesson 172) - Redox half-equations
b = LessonBlock.objects.get(id=5508)
t = b.content.get('text', '')
lines = t.split('\n')
new_lines = []
for l in lines:
    ls = l.strip()
    if ls.startswith(r'\text{MnO}_4^-') or ls.startswith(r'\text{Fe}^{2+}') or ls.startswith(r'\text{MnO}_4^- + 5\text{Fe}'):
        new_lines.append(f"$${ls}$$")
    else:
        new_lines.append(l)
b.content['text'] = '\n'.join(new_lines)
b.save()
print("Fixed Block 5508")

print("All specific leak blocks patched successfully!")
