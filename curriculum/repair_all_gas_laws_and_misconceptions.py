import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

# 1. Clean all control characters database-wide
print("Phase 1: Sanitizing all control characters database-wide...")
ctrl_fixed = 0
for b in LessonBlock.objects.all():
    raw = json.dumps(b.content)
    # Check for \x0c, \x0b, \x08, \x07, or corrupted ' imes' or 'rac'
    if any(c in raw for c in ['\\u000c', '\\u000b', '\\u0008', '\\u0007', '\x0c', '\x0b', '\x08', '\x07']) or ' imes' in raw or 'rac{' in raw:
        # Clean the string
        cleaned_raw = raw.replace('\\u000c', '\\\\f').replace('\x0c', '\\\\f')
        cleaned_raw = cleaned_raw.replace('\\u000b', '\\\\v').replace('\x0b', '\\\\v')
        cleaned_raw = cleaned_raw.replace('\\u0008', '\\\\b').replace('\x08', '\\\\b')
        cleaned_raw = cleaned_raw.replace('\\u0007', '\\\\a').replace('\x07', '\\\\a')
        cleaned_raw = re.sub(r'(?<!\\)frac\{', r'\\frac{', cleaned_raw)
        cleaned_raw = re.sub(r'\bimes\b', r'\\times', cleaned_raw)
        
        try:
            b.content = json.loads(cleaned_raw)
            b.save()
            ctrl_fixed += 1
            print(f"  Fixed control chars in Block {b.id} ({b.block_type}) in Lesson {b.lesson_id}")
        except Exception as e:
            print(f"  Error parsing Block {b.id}: {e}")

print(f"Total control character blocks fixed: {ctrl_fixed}")

# 2. Specifically restore exact authentic text for all Gas Laws (Lessons 159-163) from ingest_form3_chemistry.py
print("\nPhase 2: Restoring exact authentic text for Gas Laws modules from ingest_form3_chemistry.py...")
from curriculum.ingest_form3_chemistry import CURRICULUM_DATA

for topic in CURRICULUM_DATA:
    for unit in topic.get("units", []):
        unit_title = unit.get("lesson_title")
        try:
            lesson = Lesson.objects.get(title__icontains=unit_title)
        except Lesson.DoesNotExist:
            continue
        except Lesson.MultipleObjectsReturned:
            lesson = Lesson.objects.filter(title__icontains=unit_title).first()
            
        print(f"\nRe-aligning Lesson {lesson.id}: {lesson.title}")
        for card in unit.get("cards", []):
            card_title = card.get("page_title")
            card_type = card.get("block_type")
            card_content = card.get("content")
            
            # Find matching block in lesson
            matching_blocks = lesson.blocks.filter(title=card_title, block_type=card_type)
            if not matching_blocks.exists():
                matching_blocks = lesson.blocks.filter(title=card_title)
                
            for mb in matching_blocks:
                mb.content = card_content
                mb.save()
                print(f"  Synced Block {mb.id} ({mb.block_type}): {mb.title}")

# 3. Check all common_misconceptions database-wide for any prose trapped inside $...$ or broken LaTeX
print("\nPhase 3: Auditing ALL common_misconception blocks database-wide...")
COMMON_WORDS = set(['the', 'and', 'that', 'have', 'for', 'not', 'with', 'you', 'this', 'but', 'his', 'from', 'they', 'say', 'her', 'she', 'will', 'one', 'all', 'would', 'there', 'their', 'what', 'out', 'about', 'who', 'get', 'which', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'inverse', 'relationship', 'cut', 'half', 'double', 'doubles', 'doubling', 'pressure', 'volume', 'temperature'])

mis_fixed = 0
for b in LessonBlock.objects.filter(block_type='common_misconception'):
    raw = json.dumps(b.content)
    text_val = b.content.get('text', '') if isinstance(b.content, dict) else (b.content if isinstance(b.content, str) else '')
    if not text_val: continue
    
    # Check if there is an unmatched $ or prose in $
    # Find all inline $...$
    math_matches = re.findall(r'\$([^\$\n]+)\$', text_val)
    needs_fix = False
    for mm in math_matches:
        words = re.findall(r'[a-zA-Z]{3,}', mm)
        prose_words = [w.lower() for w in words if w.lower() in COMMON_WORDS]
        if len(prose_words) >= 2:
            needs_fix = True
            break
            
    if needs_fix or text_val.count('$') % 2 != 0:
        print(f"  [MISCONCEPTION ISSUE] Block {b.id} in Lesson {b.lesson_id}: {b.title}")
        print(f"     Text snippet: {text_val[:150]}")

print("\nAudit completed!")
