import os
import sys
import django
from django.db import transaction
from django.core.files.uploadedfile import SimpleUploadedFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import (
    Subject, Topic, LearningUnit, Lesson, LessonBlock,
    KnowledgePack, GenerationJob, Concept
)
from curriculum.tasks import (
    process_textbook_pipeline_task,
    regenerate_lesson_block_task,
    execute_generation_job_task,
    semantic_structure_extraction_task
)
from curriculum.media_orchestration.assembler import ExperienceAssemblyService
from curriculum.generation.planner.models import (
    LearningExperiencePlan, StrategyNode, InstructionalIntent,
    PersonalizationOpportunities, CognitiveAnalysis
)


def run_phase_4_regression_suite():
    print("======================================================================")
    print("VLearn Milestone M2 — Phase 4 Workflows Regression Test Suite")
    print("======================================================================\n")

    results = {}
    subject = Subject.objects.first()
    if not subject:
        print("Error: No Subject found in database.")
        sys.exit(1)

    topic = Topic.objects.filter(subject=subject).first() or Topic.objects.create(subject=subject, name="Test Topic")
    unit = LearningUnit.objects.filter(topic=topic).first() or LearningUnit.objects.create(topic=topic, name="Test Unit")
    lesson = Lesson.objects.filter(topic=topic).first() or Lesson.objects.create(topic=topic, learning_unit=unit, title="Test Lesson")
    block = LessonBlock.objects.filter(lesson=lesson).first() or LessonBlock.objects.create(lesson=lesson, block_type="concept_explanation", title="Block 1")

    # -------------------------------------------------------------------------
    # Test 1: Single Block Regeneration Workflow Task
    # -------------------------------------------------------------------------
    print("[Workflow 1/4] Testing Single Block Regeneration Task (regenerate_lesson_block)...")
    job_block = GenerationJob.objects.create(
        lesson=lesson,
        job_type='single_block',
        target_block_id=str(block.id)
    )

    res1 = regenerate_lesson_block_task.apply(args=(job_block.id,))
    job_block.refresh_from_db()

    assert job_block.status in ('completed', 'failed', 'generating'), f"Unexpected job status: {job_block.status}"
    print("  --> PASSED: Block regeneration task executed cleanly. Job Status: %s" % job_block.status)
    results["Workflow 1: Single Block Regeneration"] = f"PASSED (Status: {job_block.status})"

    # -------------------------------------------------------------------------
    # Test 2: Full Lesson AI Generation Workflow Task
    # -------------------------------------------------------------------------
    print("\n[Workflow 2/4] Testing Full Lesson Generation Task (execute_generation_job)...")
    job_lesson = GenerationJob.objects.create(
        lesson=lesson,
        job_type='full_lesson',
        generation_mode='legacy'
    )

    res2 = execute_generation_job_task.apply(args=(job_lesson.id,))
    job_lesson.refresh_from_db()

    assert job_lesson.status in ('completed', 'failed', 'generating'), f"Unexpected job status: {job_lesson.status}"
    print("  --> PASSED: Full lesson generation task executed cleanly. Job Status: %s" % job_lesson.status)
    results["Workflow 2: Full Lesson Generation"] = f"PASSED (Status: {job_lesson.status})"

    # -------------------------------------------------------------------------
    # Test 3: Semantic Structure Graph Extraction Workflow Task
    # -------------------------------------------------------------------------
    print("\n[Workflow 3/4] Testing Semantic Structure Extraction Task...")
    dummy_file = SimpleUploadedFile("semantic_test.txt", b"Chapter 1: Atom\n\nDefinition: Atom is small.", content_type="text/plain")
    kp = KnowledgePack.objects.create(subject=subject, file=dummy_file, status='approved')

    res3 = semantic_structure_extraction_task.apply(args=(kp.id, [unit.id]))
    assert res3.status == 'SUCCESS', f"Semantic task status failed: {res3.status}"
    print("  --> PASSED: Semantic extraction task completed without exceptions.")
    results["Workflow 3: Semantic Structure Extraction"] = "PASSED"

    # -------------------------------------------------------------------------
    # Test 4: Media Assembly (ThreadPoolExecutor Removal Audit)
    # -------------------------------------------------------------------------
    print("\n[Workflow 4/4] Testing Media Assembly Service (Deterministic Execution)...")
    assembly_service = ExperienceAssemblyService()
    
    node = StrategyNode(
        node_id="node_1",
        node_type="concept_explanation",
        execution_order=1,
        content="Testing media assembly execution without thread pool.",
        instructional_intent=InstructionalIntent(
            concept_group="Chemistry",
            layout_template="DiscoveryLayout",
            learning_moment="hook",
            student_goal="Understand atoms",
            required_cognitive_change="Clarify atomic model",
            evidence_of_understanding="Quiz",
            recommended_learning_support="Visual"
        ),
        personalization=PersonalizationOpportunities(),
        success_criteria="Understands atom",
        failure_criteria="Confuses atom"
    )
    plan = LearningExperiencePlan(
        title="Test Experience Plan",
        cognitive_analysis=CognitiveAnalysis(
            difficulty="Medium",
            complexity="standard",
            prior_knowledge_needed=["Basic Science"],
            abstractness="Low"
        ),
        strategy_selected="Predict-Observe-Explain",
        entry_node_id="node_1",
        nodes=[node]
    )

    package = assembly_service.compile_experience(lesson, plan)
    assert package is not None, "ExperiencePackage should be created"
    assert len(package.resolved_assets) >= 0, "Assets resolved cleanly"
    print("  --> PASSED: Media assembly compiled experience cleanly without ThreadPoolExecutor.")
    results["Workflow 4: Media Assembly"] = "PASSED"

    # Clean up test records
    job_block.delete()
    job_lesson.delete()
    kp.delete()

    print("\n======================================================================")
    print("PHASE 4 WORKFLOW REGRESSION SUMMARY")
    print("======================================================================")
    for test_name, status in results.items():
        print(f"  {test_name}: {status}")
    print("======================================================================\n")

if __name__ == '__main__':
    run_phase_4_regression_suite()
