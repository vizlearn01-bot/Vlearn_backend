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

blocks = LessonBlock.objects.filter(lesson__in=lessons).select_related('lesson').order_by('id')

print(f"Total Chemistry Blocks Scanned: {blocks.count()}")

xr_list = []
title_latex_list = []
unwrapped_eqs_list = []

for b in blocks:
    content_str = json.dumps(b.content) if isinstance(b.content, (dict, list)) else str(b.content or '')
    title_str = str(b.title or '')
    page_title_str = str(b.page_title or '')

    # Check for \xr in content/title/page_title
    if r'\xr' in content_str or r'\xr' in title_str or r'\xr' in page_title_str:
        xr_list.append((b.id, b.lesson.id, b.lesson.title, content_str))

    # Check for LaTeX in title or page_title
    if any(kw in title_str or kw in page_title_str for kw in [r'\text', r'\Delta', r'\rightarrow', r'\frac', r'^{', r'_{']):
        title_latex_list.append((b.id, b.lesson.id, b.lesson.title, b.title, b.page_title))

print(f"\n1. Blocks with corrupted '\\xr' arrows: {len(xr_list)}")
for item in xr_list[:10]:
    c = item[3]
    idx = c.find(r'\xr')
    snippet = c[max(0, idx-40):min(len(c), idx+80)]
    print(f"   Block [{item[0]}] in Lesson [{item[1]}] \"{item[2]}\":")
    print(f"      {repr(snippet)}")

print(f"\n2. Blocks with raw LaTeX in title/page_title: {len(title_latex_list)}")
for item in title_latex_list[:10]:
    print(f"   Block [{item[0]}] in Lesson [{item[1]}] \"{item[2]}\":")
    print(f"      Title: {repr(item[3])}")
    print(f"      PageTitle: {repr(item[4])}")
