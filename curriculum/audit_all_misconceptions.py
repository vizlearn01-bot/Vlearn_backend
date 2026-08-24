import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson

print("=== Auditing all Gas Law modules and all common_misconception blocks ===")

# Check Gas Laws lessons (159 to 163)
gas_lessons = Lesson.objects.filter(id__in=[159, 160, 161, 162, 163])
for les in gas_lessons:
    print(f"\n--- Lesson {les.id}: {les.title} ---")
    for b in les.blocks.all().order_by('page_number', 'order'):
        raw = json.dumps(b.content)
        # Check for \x0c, \x09, \x0b, or unmatched $
        has_ctrl = any(c in raw for c in ['\\u000c', '\\u0009', '\\u000b', '\\u0008', '\\u0007', '\x0c', '\x09', '\x0b', '\x08', '\x07'])
        if has_ctrl or 'imes' in raw or 'rac{' in raw:
            print(f"  [CORRUPTED] Block {b.id} ({b.block_type}) Page {b.page_number} Order {b.order}: {b.title}")
            print(f"     Content: {raw[:200]}")
