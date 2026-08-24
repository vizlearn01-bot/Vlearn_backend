import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset, Simulation

# 1. Fetch Lesson 68 ("Equilibrium") and Simulation "chemical_equilibrium"
lesson = Lesson.objects.get(id=68)
sim = Simulation.objects.get(key='chemical_equilibrium')

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
sim_block.title = 'Chemical Equilibrium'
sim_block.page_title = 'Interactive Simulation: Chemical Equilibrium'
sim_block.page_number = 6
sim_block.order = 6
sim_block.component_order = 1
sim_block.content = {
    'simulation_key': 'chemical_equilibrium',
    'archetype': 'chemical_equilibrium',
    'title': 'Chemical Equilibrium',
    'subject': 'CHEMISTRY',
    'topic': 'Reaction Rates and Reversible Reactions',
    'config': sim.config
}
sim_block.metadata = {
    'simulation_key': 'chemical_equilibrium',
    'archetype': 'chemical_equilibrium',
    'subject': 'CHEMISTRY',
    'concept_group': 'Interactive Simulation: Chemical Equilibrium',
    'config': sim.config
}
sim_block.save()
print(f"Saved Simulation Block: Block [{sim_block.id}]")

# 3. Update orders and page numbers of subsequent Knowledge Check and Summary blocks
# Block 1750 (Check Your Understanding MCQ 1) -> page_number=7, order=7
b1750 = LessonBlock.objects.filter(id=1750).first()
if b1750:
    b1750.page_number = 7
    b1750.order = 7
    b1750.save(update_fields=['page_number', 'order'])

# Block 1751 (Check Your Understanding MCQ 2) -> page_number=8, order=8
b1751 = LessonBlock.objects.filter(id=1751).first()
if b1751:
    b1751.page_number = 8
    b1751.order = 8
    b1751.save(update_fields=['page_number', 'order'])

# Block 1753 (Practice Question) -> page_number=9, order=9
b1753 = LessonBlock.objects.filter(id=1753).first()
if b1753:
    b1753.page_number = 9
    b1753.order = 9
    b1753.save(update_fields=['page_number', 'order'])

# Block 1755 (Answer) -> page_number=11, order=11
b1755 = LessonBlock.objects.filter(id=1755).first()
if b1755:
    b1755.page_number = 11
    b1755.order = 11
    b1755.save(update_fields=['page_number', 'order'])

# Block 1756 (Module Summary) -> page_number=12, order=12
b1756 = LessonBlock.objects.filter(id=1756).first()
if b1756:
    b1756.page_number = 12
    b1756.order = 12
    b1756.save(update_fields=['page_number', 'order'])

# 4. Attach/create LessonAsset for this simulation block
asset, created = LessonAsset.objects.get_or_create(
    lesson=lesson,
    asset_type='simulation',
    defaults={
        'source_type': 'knowledge_repository',
        'storage_type': 'url',
        'status': 'attached',
        'title': 'Chemical Equilibrium',
        'url': 'simulation://chemical_equilibrium',
        'metadata': {
            'simulation_key': 'chemical_equilibrium',
            'archetype': 'chemical_equilibrium',
            'config': sim.config
        }
    }
)
if not created:
    asset.url = 'simulation://chemical_equilibrium'
    asset.metadata = {
        'simulation_key': 'chemical_equilibrium',
        'archetype': 'chemical_equilibrium',
        'config': sim.config
    }
    asset.status = 'attached'
    asset.save()

asset.blocks.add(sim_block)
print(f"Attached LessonAsset [{asset.id}] to Simulation Block [{sim_block.id}]")

print("\n=== UPDATED LESSON 68 BLOCKS ===")
for b in LessonBlock.objects.filter(lesson=lesson).order_by('order'):
    print(f"Block [{b.id}] order={b.order:<2}, page_number={b.page_number:<2}, type={b.block_type:<24}, page_title=\"{b.page_title}\": \"{b.title}\"")
