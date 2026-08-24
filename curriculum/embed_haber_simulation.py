import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset, Simulation

# 1. Fetch Lesson 75 ("The Haber Process") and Simulation "chem_haber_process_optimizer"
lesson = Lesson.objects.get(id=75)
sim = Simulation.objects.get(key='chem_haber_process_optimizer')

print(f"Target Lesson: [{lesson.id}] {lesson.title}")
print(f"Simulation: [{sim.key}] {sim.title}")

# 2. Check if a simulation block already exists in this lesson (for idempotency)
existing_sim_blocks = LessonBlock.objects.filter(
    lesson=lesson,
    block_type__in=['suggested_simulation', 'simulation_placeholder']
)

if existing_sim_blocks.exists():
    sim_block = existing_sim_blocks.first()
    print(f"Simulation block already exists: Block [{sim_block.id}]. Updating...")
else:
    sim_block = LessonBlock(lesson=lesson)

sim_block.block_type = 'suggested_simulation'
sim_block.component_type = 'suggested_simulation'
sim_block.title = 'Industrial Optimization: The Haber Process'
sim_block.page_title = 'Interactive Simulation: Industrial Optimization'
sim_block.page_number = 4
sim_block.order = 4
sim_block.component_order = 1
sim_block.content = {
    'simulation_key': 'chem_haber_process_optimizer',
    'archetype': 'chem_haber_process_optimizer',
    'title': 'Industrial Optimization: The Haber Process',
    'subject': 'CHEMISTRY',
    'topic': 'Reaction Rates and Reversible Reactions',
    'config': sim.config
}
sim_block.metadata = {
    'simulation_key': 'chem_haber_process_optimizer',
    'archetype': 'chem_haber_process_optimizer',
    'subject': 'CHEMISTRY',
    'concept_group': 'Interactive Simulation: The Haber Process',
    'config': sim.config
}
sim_block.save()
print(f"Saved Simulation Block: Block [{sim_block.id}]")

# 3. Update orders and page numbers of subsequent Knowledge Check and Summary blocks
# Block 1821 (Check Your Understanding 1) -> page_number=5, order=5
b1821 = LessonBlock.objects.filter(id=1821).first()
if b1821:
    b1821.page_number = 5
    b1821.order = 5
    b1821.save(update_fields=['page_number', 'order'])

# Block 5870 (Diagram) -> page_number=5
b5870 = LessonBlock.objects.filter(id=5870).first()
if b5870:
    b5870.page_number = 5
    b5870.save(update_fields=['page_number'])

# Block 1822 (Practice Questions & Analysis) -> page_number=6, order=6
b1822 = LessonBlock.objects.filter(id=1822).first()
if b1822:
    b1822.page_number = 6
    b1822.order = 6
    b1822.save(update_fields=['page_number', 'order'])

# Block 1826 (Module Summary) -> page_number=7, order=7
b1826 = LessonBlock.objects.filter(id=1826).first()
if b1826:
    b1826.page_number = 7
    b1826.order = 7
    b1826.save(update_fields=['page_number', 'order'])

# 4. Attach/create LessonAsset for this simulation block
asset, created = LessonAsset.objects.get_or_create(
    lesson=lesson,
    asset_type='simulation',
    defaults={
        'source_type': 'knowledge_repository',
        'storage_type': 'url',
        'status': 'attached',
        'title': 'Industrial Optimization: The Haber Process',
        'url': 'simulation://chem_haber_process_optimizer',
        'metadata': {
            'simulation_key': 'chem_haber_process_optimizer',
            'archetype': 'chem_haber_process_optimizer',
            'config': sim.config
        }
    }
)
if not created:
    asset.url = 'simulation://chem_haber_process_optimizer'
    asset.metadata = {
        'simulation_key': 'chem_haber_process_optimizer',
        'archetype': 'chem_haber_process_optimizer',
        'config': sim.config
    }
    asset.status = 'attached'
    asset.save()

asset.blocks.add(sim_block)
print(f"Attached LessonAsset [{asset.id}] to Simulation Block [{sim_block.id}]")

print("\n=== UPDATED LESSON 75 BLOCKS ===")
for b in LessonBlock.objects.filter(lesson=lesson).order_by('order'):
    print(f"Block [{b.id}] order={b.order}, page_number={b.page_number}, type={b.block_type:<22}, page_title=\"{b.page_title}\": \"{b.title}\"")
