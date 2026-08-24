import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock

lessons = Lesson.objects.filter(
    topic__subject__name='Chemistry',
    topic__subject__grade__name__in=['Form 3', 'Form 4']
).select_related('topic', 'topic__subject', 'topic__subject__grade').order_by('id')

print(f"Total Form 3 & Form 4 Chemistry Lessons: {lessons.count()}")

blocks = LessonBlock.objects.filter(lesson__in=lessons).select_related('lesson').order_by('id')
print(f"Total LessonBlocks: {blocks.count()}")

patterns = {
    "xr_corrupted_arrows": re.compile(r'\\xr[a-zA-Z\\]*'),
    "asterisk_subscripts": re.compile(r'(\\\w+|\})\s*\*\s*\{'),
    "escaped_underscores_carets": re.compile(r'\\[_\^]\{|\\[_\^]\('),
    "raw_latex_brackets": re.compile(r'\\\(|\\\)|\\\[|\\\]'),
    "raw_unwrapped_text_commands": re.compile(r'\\text\{[^}]+\}'),
    "raw_unwrapped_frac_commands": re.compile(r'\\frac\{[^}]+\}\{[^}]+\}'),
    "raw_arrows": re.compile(r'\\rightarrow|\\rightleftharpoons|\\leftarrow'),
    "delta_notation": re.compile(r'\\Delta\b|\bDelta\s*H'),
    "latex_env": re.compile(r'\\begin\{|\\end\{'),
    "degree_circ": re.compile(r'\^\s*\\circ|\^\\circ|\\circ'),
    "chemical_isotopes": re.compile(r'\^\s*\{?[0-9]+\}?\s*_\s*\{?[0-9]+\}?'),
}

findings = {k: [] for k in patterns}
raw_text_samples = []

for b in blocks:
    content = b.content
    content_str = json.dumps(content) if isinstance(content, (dict, list)) else str(content or '')
    title_str = str(b.title or '')
    combined = f"{title_str} {content_str}"

    for k, pat in patterns.items():
        m = pat.findall(combined)
        if m:
            findings[k].append({
                "block_id": b.id,
                "lesson_id": b.lesson.id,
                "lesson_title": b.lesson.title,
                "matches": m[:5]
            })

    # Specifically check if LaTeX exists OUTSIDE $ or $$
    # Strip properly formed $$ ... $$ and $ ... $
    stripped = re.sub(r'\$\$.*?\$\$', '', combined, flags=re.DOTALL)
    stripped = re.sub(r'\$.*?\$', '', stripped)
    
    # Check for leaked LaTeX in stripped text
    if any(kw in stripped for kw in [r'\text{', r'\frac{', r'\rightarrow', r'\rightleftharpoons', r'\Delta', r'^\circ', r'^{', r'_{', r'\xr']):
        raw_text_samples.append({
            "block_id": b.id,
            "lesson_id": b.lesson.id,
            "lesson_title": b.lesson.title,
            "snippet": stripped[:200]
        })

print("\n" + "=" * 80)
print("DIAGNOSTIC REPORT: FORM 3 & FORM 4 CHEMISTRY LATEX AUDIT")
print("=" * 80)

for k, items in findings.items():
    print(f"[{k}]: {len(items)} blocks affected")
    if items:
        ex = items[0]
        print(f"   Example: Block {ex['block_id']} in Lesson {ex['lesson_id']} \"{ex['lesson_title']}\"")
        print(f"   Matches: {ex['matches']}")

print("\n" + "=" * 80)
print(f"TOTAL BLOCKS WITH UNWRAPPED / LEAKING LATEX: {len(raw_text_samples)}")
print("=" * 80)

for s in raw_text_samples[:10]:
    print(f"Block [{s['block_id']}] (Lesson {s['lesson_id']} - {s['lesson_title']}):")
    print(f"  Snippet: {repr(s['snippet'])}")
    print("-" * 40)
