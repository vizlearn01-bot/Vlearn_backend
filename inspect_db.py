import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import *

print("--- DB Stats ---")
print(f"KnowledgePacks: {KnowledgePack.objects.count()}")
print(f"LearningUnits: {LearningUnit.objects.count()}")
print(f"Lessons: {Lesson.objects.count()}")
print(f"GenerationJobs: {GenerationJob.objects.count()}")
print(f"LearningExperienceGraphs: {LearningExperienceGraph.objects.count()}")
print(f"LessonBlocks: {LessonBlock.objects.count()}")

# Get the latest completed GenerationJob
job = GenerationJob.objects.filter(status='completed').order_by('-created_at').first()
if job:
    print(f"\n--- Latest Completed GenerationJob: {job.id} ---")
    print(f"Lesson: {job.lesson.title}")
    
    lu = job.lesson.learning_unit
    from curriculum.generation.planner.knowledge_assembler import KnowledgeAssembler
    context = KnowledgeAssembler.assemble(lu.id)
    chunks = context['knowledge']
    total_chunks = sum(len(c) for c in chunks.values())
    print(f"\nStage 1 - Knowledge Pack Audit")
    print(f"Retrieved {total_chunks} chunks.")
    
    graph = LearningExperienceGraph.objects.filter(generation_job=job).first()
    if graph:
        print(f"\nStage 3 - Learning Experience Planner Output")
        plan = graph.graph_data
        nodes = plan.get('nodes', [])
        print(f"Nodes produced: {len(nodes)}")
        moments = set(n.get('concept_group') for n in nodes if n.get('concept_group'))
        print(f"Learning Moments (concept_groups): {len(moments)}")
        
    blocks = LessonBlock.objects.filter(lesson=job.lesson)
    print(f"\nStage 6 - Experience Assembly")
    print(f"Lesson Blocks persisted: {blocks.count()}")
else:
    print("No completed jobs found.")
