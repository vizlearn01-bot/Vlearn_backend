r"""
VLearn Universal Chemistry — Deep Equation Splitter & Arrow Sanitizer
Resolves adjacent $$ blocks stuck together (e.g. $$Eq1$$Eq2$$ -> $$Eq1$$\n\n$$Eq2$$)
and converts bracket/brace arrows (\rightarrow{\text{heat}} -> \xrightarrow{\text{heat}}).
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_equation_text(text):
    if not isinstance(text, str):
        return text

    # 1. Convert \rightarrow{condition} -> \xrightarrow{condition}
    text = re.sub(r'\\rightarrow\{([^}]+)\}', r'\\xrightarrow{\1}', text)
    # Convert \rightarrow[below]{above} -> \xrightarrow[below]{above}
    text = re.sub(r'\\rightarrow\[([^\]]+)\]\{([^}]+)\}', r'\\xrightarrow[\1]{\2}', text)

    # 2. Fix consecutive joined $$ equations on the same line: e.g. $$Eq1$$Eq2$$ or $$Eq1$$2\text{Pb...}$$
    # Replace $$(.*?)\$\$([0-9a-zA-Z\\].*?)\$\$ with $$\n\1\n$$\n\n$$\n\2\n$$
    def split_joined_math(match):
        eq1 = match.group(1).strip()
        eq2 = match.group(2).strip()
        return f"$$\n{eq1}\n$$\n\n$$\n{eq2}\n$$"

    text = re.sub(r'\$\$(.+?)\$\$([0-9a-zA-Z\\][^\$\n]+?)\$\$', split_joined_math, text)

    # 3. Clean up Block 3538 leaked practice questions at bottom if present
    if "📝 Understanding Check" in text and "🗝️ Explanations & Answers" in text:
        text = text.split("📝 Understanding Check")[0].strip()

    # 4. Clean up Block 3802 equation annotations
    text = text.replace(r'$$ \text{(Soluble Soap)} + \text{(Calcium Ions)} \rightarrow \mathbf{ \text{Calcium Stearate (Insoluble Scum)}} + \text{(Sodium Ions)}$$',
                        r'$$\text{Soluble Soap} + \text{Calcium Ions} \rightarrow \text{Calcium Stearate (Scum)} + \text{Sodium Ions}$$')
    text = text.replace(r'$$ \text{(Soluble Soap)} + \text{(Magnesium Ions)} \rightarrow \mathbf{ \text{Magnesium Stearate (Insoluble Scum)}} + \text{(Sodium Ions)}$$',
                        r'$$\text{Soluble Soap} + \text{Magnesium Ions} \rightarrow \text{Magnesium Stearate (Scum)} + \text{Sodium Ions}$$')

    # 5. Clean up Block 5643 sulphur equations
    text = text.replace(r'$$\Delta T = 113 - 25 = 88^\circ\text{C}$$Q_1 = m \times c \times \Delta T = 1000\text{ g} \times 0.71\text{ J g}^{-1\circ}\text{C}^{-1} \times 88^\circ\text{C} = 62,480\text{ J} = 62.48\text{ kJ}$$',
                        r'$$\Delta T = 113 - 25 = 88^\circ\text{C}$$$$Q_1 = m \times c \times \Delta T = 1000\text{ g} \times 0.71\text{ J g}^{-1\circ}\text{C}^{-1} \times 88^\circ\text{C} = 62,480\text{ J} = 62.48\text{ kJ}$$')

    return text

def recursive_clean_obj(val):
    if isinstance(val, str):
        return clean_equation_text(val)
    elif isinstance(val, dict):
        return {k: recursive_clean_obj(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [recursive_clean_obj(i) for i in val]
    return val

def run_deep_clean():
    print("=" * 80)
    print("RUNNING DEEP EQUATION SPLITTER & ARROW SANITIZER")
    print("=" * 80)

    blocks = LessonBlock.objects.filter(
        lesson__topic__subject__name='Chemistry',
        lesson__topic__subject__grade__name__in=['Form 3', 'Form 4']
    )

    cleaned_count = 0
    for b in blocks:
        if not b.content:
            continue
        new_c = recursive_clean_obj(b.content)
        if new_c != b.content:
            b.content = new_c
            b.save(update_fields=['content'])
            cleaned_count += 1

    print(f"[*] Successfully sanitized {cleaned_count} blocks with joined equations or custom arrow braces.")
    print("=" * 80)

if __name__ == "__main__":
    run_deep_clean()
