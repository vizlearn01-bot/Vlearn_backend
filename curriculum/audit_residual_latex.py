import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

blocks = LessonBlock.objects.filter(
    lesson__topic__subject__name='Chemistry',
    lesson__topic__subject__grade__name__in=['Form 3', 'Form 4']
).select_related('lesson').order_by('id')

leaked_blocks = []

for b in blocks:
    content_str = json.dumps(b.content) if isinstance(b.content, (dict, list)) else str(b.content or '')
    title_str = str(b.title or '')
    page_title_str = str(b.page_title or '')
    combined = f"{title_str} {page_title_str} {content_str}"
    
    # Strip valid KaTeX math
    stripped = re.sub(r'\$\$.*?\$\$', '', combined, flags=re.DOTALL)
    stripped = re.sub(r'\$.*?\$', '', stripped)
    
    # Check for actual LaTeX command keywords outside math
    latex_keywords = [
        r'\text{', r'\frac{', r'\rightarrow', r'\rightleftharpoons', r'\leftarrow',
        r'\xrightarrow', r'\Delta', r'\alpha', r'\beta', r'\gamma', r'\theta',
        r'\approx', r'\times', r'\pm', r'\circ', r'^{', r'_{', r'\xr'
    ]
    
    found = [kw for kw in latex_keywords if kw in stripped]
    if found:
        leaked_blocks.append({
            "id": b.id,
            "lesson_id": b.lesson.id,
            "lesson_title": b.lesson.title,
            "keywords": found,
            "snippet": stripped[:200]
        })

print("=" * 80)
print(f"RESIDUAL LATEX SCAN RESULTS (Form 3 & Form 4 Chemistry):")
print(f"Total blocks with unescaped LaTeX outside math: {len(leaked_blocks)}")
print("=" * 80)

for l in leaked_blocks:
    print(f"Block [{l['id']}] (Lesson {l['lesson_id']} \"{l['lesson_title']}\"):")
    print(f"  Keywords: {l['keywords']}")
    print(f"  Snippet:  {repr(l['snippet'])}")
    print("-" * 50)
