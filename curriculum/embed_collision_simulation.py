import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset, Simulation

# 1. Fetch Lesson 64 ("Collision Theory and Activation Energy") and Simulation "chem_collision_theory_kinetics"
lesson = Lesson.objects.get(id=64)
sim = Simulation.objects.get(key='chem_collision_theory_kinetics')

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
sim_block.title = 'Collision Theory & Activation Energy'
sim_block.page_title = 'Interactive Simulation: Collision Theory'
sim_block.page_number = 6
sim_block.order = 6
sim_block.component_order = 1
sim_block.content = {
    'simulation_key': 'chem_collision_theory_kinetics',
    'archetype': 'collision_theory_kinetics',
    'title': 'Collision Theory & Activation Energy',
    'subject': 'CHEMISTRY',
    'topic': 'Reaction Rates and Reversible Reactions',
    'config': sim.config
}
sim_block.metadata = {
    'simulation_key': 'chem_collision_theory_kinetics',
    'archetype': 'collision_theory_kinetics',
    'subject': 'CHEMISTRY',
    'concept_group': 'Interactive Simulation: Collision Theory',
    'config': sim.config
}
sim_block.save()
print(f"Saved Simulation Block: Block [{sim_block.id}]")

# 3. Update orders and page numbers of subsequent Knowledge Check and Summary blocks
# Block 1688 (Check Your Understanding Header) -> page_number=7, order=7
b1688 = LessonBlock.objects.filter(id=1688).first()
if b1688:
    b1688.page_number = 7
    b1688.order = 7
    b1688.save(update_fields=['page_number', 'order'])

# Block 1689 (Check Your Understanding MCQ) -> page_number=7, order=8
b1689 = LessonBlock.objects.filter(id=1689).first()
if b1689:
    b1689.page_number = 7
    b1689.order = 8
    b1689.save(update_fields=['page_number', 'order'])

# Block 1690 (Misconception Buster) -> page_number=8, order=9
b1690 = LessonBlock.objects.filter(id=1690).first()
if b1690:
    b1690.page_number = 8
    b1690.order = 9
    b1690.save(update_fields=['page_number', 'order'])

# Block 1691 (Practice Questions & Analysis) -> page_number=9, order=10
b1691 = LessonBlock.objects.filter(id=1691).first()
if b1691:
    b1691.page_number = 9
    b1691.order = 10
    b1691.save(update_fields=['page_number', 'order'])

# Block 1693 (The two requirements are:) -> page_number=10, order=11
b1693 = LessonBlock.objects.filter(id=1693).first()
if b1693:
    b1693.page_number = 10
    b1693.order = 11
    b1693.save(update_fields=['page_number', 'order'])

# Block 1694 (Module Summary) -> page_number=11, order=12
b1694 = LessonBlock.objects.filter(id=1694).first()
if b1694:
    b1694.page_number = 11
    b1694.order = 12
    b1694.save(update_fields=['page_number', 'order'])

# 4. Attach/create LessonAsset for this simulation block
asset, created = LessonAsset.objects.get_or_create(
    lesson=lesson,
    asset_type='simulation',
    defaults={
        'source_type': 'knowledge_repository',
        'storage_type': 'url',
        'status': 'attached',
        'title': 'Collision Theory & Activation Energy',
        'url': 'simulation://chem_collision_theory_kinetics',
        'metadata': {
            'simulation_key': 'chem_collision_theory_kinetics',
            'archetype': 'collision_theory_kinetics',
            'config': sim.config
        }
    }
)
if not created:
    asset.url = 'simulation://chem_collision_theory_kinetics'
    asset.metadata = {
        'simulation_key': 'chem_collision_theory_kinetics',
        'archetype': 'collision_theory_kinetics',
        'config': sim.config
    }
    asset.status = 'attached'
    asset.save()

asset.blocks.add(sim_block)
print(f"Attached LessonAsset [{asset.id}] to Simulation Block [{sim_block.id}]")

print("\n=== UPDATED LESSON 64 BLOCKS ===")
for b in LessonBlock.objects.filter(lesson=lesson).order_by('order'):
    print(f"Block [{b.id}] order={b.order}, page_number={b.page_number}, type={b.block_type:<24}, page_title=\"{b.page_title}\": \"{b.title}\"")
