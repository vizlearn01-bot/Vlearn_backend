import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

blocks = LessonBlock.objects.filter(
    lesson__topic__subject__name='Chemistry',
    lesson__topic__subject__grade__name__in=['Form 3', 'Form 4']
).select_related('lesson').order_by('id')

def check_unwrapped_latex_in_text(raw_text):
    if not isinstance(raw_text, str) or not raw_text.strip():
        return []

    # 1. Strip $$ ... $$ display blocks
    t = re.sub(r'\$\$.*?\$\$', '', raw_text, flags=re.DOTALL)
    # 2. Strip $ ... $ inline math
    t = re.sub(r'\$[^\$\n]+?\$', '', t)

    # 3. Check for genuine leaked LaTeX syntax
    leaks = []
    
    # Check for \xr
    if r'\xr' in t:
        leaks.append(r'\xr')
    # Check for *{(s)} or \_{(s)}
    if re.search(r'\*\{\([a-zA-Z]+\)\}|\\\_\{', t):
        leaks.append('malformed_subscript')
    # Check for raw \text{
    if r'\text{' in t:
        leaks.append(r'\text{')
    # Check for raw \frac{
    if r'\frac{' in t:
        leaks.append(r'\frac{')
    # Check for raw \rightarrow or \rightleftharpoons
    if r'\rightarrow' in t or r'\rightleftharpoons' in t or r'\xrightarrow' in t:
        leaks.append('raw_arrow')
    # Check for raw \Delta outside $
    if re.search(r'\\Delta\b|\bDelta\s*H', t):
        leaks.append(r'\Delta')
        
    return leaks

def extract_all_strings(obj):
    texts = []
    if isinstance(obj, str):
        texts.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            texts.extend(extract_all_strings(v))
    elif isinstance(obj, list):
        for item in obj:
            texts.extend(extract_all_strings(item))
    return texts

leaked_blocks = []

for b in blocks:
    all_texts = [b.title or '', b.page_title or ''] + extract_all_strings(b.content)
    block_leaks = []
    
    for text in all_texts:
        found = check_unwrapped_latex_in_text(text)
        if found:
            block_leaks.extend(found)
            
    if block_leaks:
        leaked_blocks.append({
            "id": b.id,
            "lesson_id": b.lesson.id,
            "lesson_title": b.lesson.title,
            "leaks": list(set(block_leaks)),
            "content_sample": str(b.content)[:200]
        })

print("=" * 80)
print("FINAL RECURSIVE REST API CONTENT AUDIT:")
print(f"Total blocks scanned: {blocks.count()}")
print(f"Total blocks with leaked LaTeX: {len(leaked_blocks)}")
print("=" * 80)

for lb in leaked_blocks:
    print(f"Block [{lb['id']}] in Lesson [{lb['lesson_id']}] \"{lb['lesson_title']}\":")
    print(f"  Leaks: {lb['leaks']}")
    print(f"  Sample: {lb['content_sample']}")
    print("-" * 50)
