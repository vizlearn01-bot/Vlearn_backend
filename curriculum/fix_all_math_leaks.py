import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Cleaning definition cards, formulas, and math blocks...")

count_fixed = 0

def clean_text(t):
    if not isinstance(t, str):
        return t
    orig = t
    
    # 1. Fix ( = P_2V_2$) or ( = P_2V_2)
    t = re.sub(r'\(\s*=\s*P_2V_2\$?\)', r'($P_1V_1 = P_2V_2$)', t)
    
    # 2. Fix whole english sentences wrapped in $$...$$ inside definition cards
    # e.g. $$Charles's Law states that ... ( ... where $ is in Kelvin).$$
    if t.startswith('$$') and t.endswith('$$') and ('states that' in t or 'is defined as' in t or 'refers to' in t):
        inner = t[2:-2].strip()
        # Remove broken stray dollars like "where $ is in Kelvin"
        inner = inner.replace('where $ is in Kelvin', 'where $T$ is in Kelvin')
        inner = inner.replace('where $ is in', 'where $T$ is in')
        t = inner
        
    # 3. Fix nested $\text{...}$ inside \frac or $$
    t = re.sub(r'\\frac\{\s*\$\\text\{([^}]+)\}\$\s*\}\s*\{\s*\$\\text\{([^}]+)\}\$\s*\}', r'\\frac{\\text{\1}}{\\text{\2}}', t)
    
    # 4. Fix markdown **...** wrapped in $...$ e.g. $**Strong Acid**: ...$
    t = re.sub(r'\$\*\*([^*]+)\*\*:\s*([^$]+)\$', r'**\1**: $\2$', t)
    
    # 5. Fix naked \text{...} = \text{...} at start of string outside math
    if t.strip().startswith(r'\text{') and '$$' not in t[:10]:
        # If it is a whole standalone line equation, wrap in $$...$$
        lines = t.split('\n')
        new_lines = []
        for line in lines:
            line_s = line.strip()
            if line_s.startswith(r'\text{') and ('=' in line_s or r'\rightarrow' in line_s):
                new_lines.append(f"$${line_s}$$")
            else:
                new_lines.append(line)
        t = '\n'.join(new_lines)
        
    # 6. Fix fused equations like $$...$$ \text{Number of Moles}...
    t = re.sub(r'(\}\s*)\$(\\text\{[A-Za-z\s]+\}\s*\([nMV]\)\s*=)', r'\1\n\n$$\2', t)
    
    # 7. Specific fixes
    # Boyle's Law definition
    if "Boyle's Law states that" in t and "inversely proportional" in t:
        t = "The volume of a fixed mass of gas is inversely proportional to its pressure, provided the temperature remains constant ($P_1V_1 = P_2V_2$)."
    if "Charles's Law states that" in t and "directly proportional" in t:
        t = "The volume of a fixed mass of gas is directly proportional to its absolute temperature (in Kelvin), provided the pressure remains constant ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$)."
    if "Graham's Law states that" in t and "inversely proportional" in t:
        t = "Under identical conditions of temperature and pressure, the rate of diffusion of a gas is inversely proportional to the square root of its density or relative molecular mass ($\\frac{R_A}{R_B} = \\sqrt{\\frac{M_B}{M_A}}$)."
        
    return t

def clean_dict(d):
    for k, v in d.items():
        if isinstance(v, str):
            d[k] = clean_text(v)
        elif isinstance(v, list):
            d[k] = [clean_text(item) if isinstance(item, str) else (clean_dict(item) if isinstance(item, dict) else item) for item in v]
        elif isinstance(v, dict):
            clean_dict(v)

for b in LessonBlock.objects.all():
    orig_content = json.dumps(b.content)
    if isinstance(b.content, dict):
        clean_dict(b.content)
    elif isinstance(b.content, str):
        b.content = clean_text(b.content)
        
    new_content = json.dumps(b.content)
    if orig_content != new_content:
        b.save()
        count_fixed += 1
        print(f"Fixed Block {b.id} ({b.block_type}) in Lesson {b.lesson_id}")

print(f"Total blocks cleaned and updated: {count_fixed}")
