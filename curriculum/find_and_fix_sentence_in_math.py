import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Auditing all blocks for English prose wrapped in $$...$$ or broken delimiters...")

LATEX_KEYWORDS = set([
    'frac', 'sqrt', 'times', 'text', 'mathrm', 'mathbf', 'approx', 'implies',
    'propto', 'rightleftharpoons', 'rightarrow', 'quad', 'qquad', 'cdot',
    'Delta', 'rho', 'alpha', 'beta', 'gamma', 'theta', 'lambda', 'sigma',
    'omega', 'over', 'left', 'right', 'circ', 'degree', 'pm', 'mp', 'le', 'ge',
    'leq', 'geq', 'neq', 'ne', 'div', 'int', 'sum', 'partial', 'mol', 'dm', 'cm',
    'kPa', 'mmHg', 'atm', 'K', 'C', 'V', 'P', 'T', 'n', 'm', 'M', 'R', 't', 's'
])

def unwrap_prose_from_display_math(text_val):
    if not isinstance(text_val, str) or '$$' not in text_val:
        return text_val
    
    def replacer(match):
        inner = match.group(1).strip()
        # Find words in inner
        words = re.findall(r'[a-zA-Z]{2,}', inner)
        non_latex = [w for w in words if w.lower() not in LATEX_KEYWORDS and w not in LATEX_KEYWORDS]
        
        # If there are 3 or more normal English words inside $$...$$, this is prose, NOT a mathematical equation!
        if len(non_latex) >= 2 or '!' in inner or '?' in inner or 'In this module' in inner or 'discover' in inner or 'explore' in inner:
            # Unwrap the display math $$
            return inner
        return match.group(0)

    # Replace $$...$$ where inner is English prose
    return re.sub(r'\$\$([\s\S]*?)\$\$', replacer, text_val)

def clean_dict(d):
    for k, v in d.items():
        if isinstance(v, str):
            d[k] = unwrap_prose_from_display_math(v)
        elif isinstance(v, list):
            d[k] = [unwrap_prose_from_display_math(item) if isinstance(item, str) else (clean_dict(item) if isinstance(item, dict) else item) for item in v]
        elif isinstance(v, dict):
            clean_dict(v)

fixed_count = 0
for b in LessonBlock.objects.all():
    orig = json.dumps(b.content)
    if isinstance(b.content, dict):
        clean_dict(b.content)
    elif isinstance(b.content, str):
        b.content = unwrap_prose_from_display_math(b.content)
        
    new = json.dumps(b.content)
    if orig != new:
        b.save()
        fixed_count += 1
        print(f"Fixed prose in $$ in Block {b.id} ({b.block_type}) in Lesson {b.lesson_id}: {b.title}")

print(f"Total blocks cleaned: {fixed_count}")
