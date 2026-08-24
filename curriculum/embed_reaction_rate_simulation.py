import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset, Simulation

# 1. Fetch Lesson 65 ("Factors Affecting the Rate of a Reaction") and Simulation "reaction_rate"
lesson = Lesson.objects.get(id=65)
sim = Simulation.objects.get(key='reaction_rate')

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
sim_block.title = 'Reaction Rate'
sim_block.page_title = 'Interactive Simulation: Reaction Rate'
sim_block.page_number = 17
sim_block.order = 24
sim_block.component_order = 1
sim_block.content = {
    'simulation_key': 'reaction_rate',
    'archetype': 'reaction_rate',
    'title': 'Reaction Rate',
    'subject': 'CHEMISTRY',
    'topic': 'Reaction Rates and Reversible Reactions',
    'config': sim.config
}
sim_block.metadata = {
    'simulation_key': 'reaction_rate',
    'archetype': 'reaction_rate',
    'subject': 'CHEMISTRY',
    'concept_group': 'Interactive Simulation: Reaction Rate',
    'config': sim.config
}
sim_block.save()
print(f"Saved Simulation Block: Block [{sim_block.id}]")

# 3. Update orders and page numbers of subsequent Knowledge Check and Summary blocks
# Block 1718 (Check Your Understanding Header) -> page_number=18, order=25
b1718 = LessonBlock.objects.filter(id=1718).first()
if b1718:
    b1718.page_number = 18
    b1718.order = 25
    b1718.save(update_fields=['page_number', 'order'])

# Block 1719 (Check Your Understanding MCQ) -> page_number=18, order=26
b1719 = LessonBlock.objects.filter(id=1719).first()
if b1719:
    b1719.page_number = 18
    b1719.order = 26
    b1719.save(update_fields=['page_number', 'order'])

# Block 1720 (Misconception Buster) -> page_number=19, order=27
b1720 = LessonBlock.objects.filter(id=1720).first()
if b1720:
    b1720.page_number = 19
    b1720.order = 27
    b1720.save(update_fields=['page_number', 'order'])

# Block 1721 (Practice Questions & Analysis) -> page_number=20, order=28
b1721 = LessonBlock.objects.filter(id=1721).first()
if b1721:
    b1721.page_number = 20
    b1721.order = 28
    b1721.save(update_fields=['page_number', 'order'])

# Block 1723 (Module Summary) -> page_number=22, order=30
b1723 = LessonBlock.objects.filter(id=1723).first()
if b1723:
    b1723.page_number = 22
    b1723.order = 30
    b1723.save(update_fields=['page_number', 'order'])

# 4. Attach/create LessonAsset for this simulation block
asset, created = LessonAsset.objects.get_or_create(
    lesson=lesson,
    asset_type='simulation',
    defaults={
        'source_type': 'knowledge_repository',
        'storage_type': 'url',
        'status': 'attached',
        'title': 'Reaction Rate',
        'url': 'simulation://reaction_rate',
        'metadata': {
            'simulation_key': 'reaction_rate',
            'archetype': 'reaction_rate',
            'config': sim.config
        }
    }
)
if not created:
    asset.url = 'simulation://reaction_rate'
    asset.metadata = {
        'simulation_key': 'reaction_rate',
        'archetype': 'reaction_rate',
        'config': sim.config
    }
    asset.status = 'attached'
    asset.save()

asset.blocks.add(sim_block)
print(f"Attached LessonAsset [{asset.id}] to Simulation Block [{sim_block.id}]")

print("\n=== UPDATED LESSON 65 BLOCKS ===")
for b in LessonBlock.objects.filter(lesson=lesson).order_by('order'):
    print(f"Block [{b.id}] order={b.order:<2}, page_number={b.page_number:<2}, type={b.block_type:<24}, page_title=\"{b.page_title}\": \"{b.title}\"")
