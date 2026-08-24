import os, sys, django, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson

les = Lesson.objects.get(id=161)
print(f"=== Current Blocks in Lesson 161 ({les.title}) ===")
for b in les.blocks.all().order_by('page_number', 'order'):
    print(f"Page {b.page_number} | Order {b.order} | Block {b.id} ({b.block_type}) | Title: {b.title}")
