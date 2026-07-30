import os
import sys
import django
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Subject, KnowledgePack, KnowledgeChunk
from curriculum.tasks import process_textbook_pipeline_task
from curriculum.api.serializers import KnowledgePackSerializer


def run_phase_2_pilot_validation():
    print("======================================================================")
    print("VLearn Milestone M2 — Phase 2 Pilot Workflow Validation Suite")
    print("======================================================================\n")

    results = {}

    # Setup test subject
    subject = Subject.objects.first()
    if not subject:
        print("Error: No Subject found in database to run test against.")
        sys.exit(1)

    # -------------------------------------------------------------------------
    # Test 1: Full Ingestion Lifecycle via Celery Task
    # -------------------------------------------------------------------------
    print("[Test 1/3] Testing End-to-End KnowledgePack Ingestion Lifecycle...")
    test_content = (
        "Chapter 1: Atomic Structure\n\n"
        "Definition: An atom is the basic unit of a chemical element.\n\n"
        "Example: Hydrogen has one proton and one electron."
    )
    dummy_file = SimpleUploadedFile("test_chemistry_textbook.txt", test_content.encode('utf-8'), content_type="text/plain")

    # Simulate API Endpoint transaction.on_commit pattern
    with transaction.atomic():
        kp = KnowledgePack.objects.create(
            subject=subject,
            file=dummy_file,
            status='processing'
        )
        task_dispatched = []
        transaction.on_commit(lambda: task_dispatched.append(process_textbook_pipeline_task.delay(kp.id)))

    assert kp.status == 'processing', "Initial status must be 'processing'"
    assert len(task_dispatched) == 1, "Task should be enqueued on transaction commit"
    task_id = task_dispatched[0].id
    print("  --> Created KnowledgePack ID %d, Task ID: %s" % (kp.id, task_id))

    # Execute task
    res = process_textbook_pipeline_task.apply(args=(kp.id,))
    assert res.status == 'SUCCESS', f"Task execution failed: {res.result}"

    kp.refresh_from_db()
    assert kp.status == 'review', f"Expected status 'review', got '{kp.status}'"
    chunks_count = KnowledgeChunk.objects.filter(knowledge_pack=kp).count()
    assert chunks_count > 0, "KnowledgeChunks should be extracted and saved"

    print("  --> Status transitioned cleanly to '%s'. Extracted %d chunks." % (kp.status, chunks_count))
    results["Test 1: Full Lifecycle Ingestion"] = "PASSED"

    # -------------------------------------------------------------------------
    # Test 2: Failure Simulation & Error Recovery (No Stuck Jobs)
    # -------------------------------------------------------------------------
    print("\n[Test 2/3] Simulating Worker Exception / File Error Handling...")
    kp_fail = KnowledgePack.objects.create(
        subject=subject,
        file=None, # Invalid: No file attached
        status='processing'
    )

    try:
        # Task will encounter Exception("No file attached to Knowledge Pack.")
        res_fail = process_textbook_pipeline_task.apply(args=(kp_fail.id,))
    except Exception as exc:
        print("  --> Expected exception caught during task execution: %s" % exc)

    kp_fail.refresh_from_db()
    assert kp_fail.status == 'failed', f"Expected status 'failed', got '{kp_fail.status}'"
    print("  --> PASSED: Failure handler caught error and set KnowledgePack.status = 'failed'")
    results["Test 2: Failure & Error State Handling"] = "PASSED"

    # -------------------------------------------------------------------------
    # Test 3: API & Serialization Contract Preserved
    # -------------------------------------------------------------------------
    print("\n[Test 3/3] Verifying API Contract & Serializer Compatibility...")
    serializer = KnowledgePackSerializer(kp)
    serialized_data = serializer.data

    assert 'id' in serialized_data, "Serializer payload must include 'id'"
    assert 'status' in serialized_data, "Serializer payload must include 'status'"
    assert serialized_data['status'] == 'review', "Serialized status must match model state"
    print("  --> PASSED: API serializer contract remains 100% compliant.")
    results["Test 3: API Contract Verification"] = "PASSED"

    # Clean up test records
    kp.delete()
    kp_fail.delete()

    print("\n======================================================================")
    print("PHASE 2 PILOT WORKFLOW VALIDATION SUMMARY")
    print("======================================================================")
    for test_name, status in results.items():
        print(f"  {test_name}: {status}")
    print("======================================================================\n")

if __name__ == '__main__':
    run_phase_2_pilot_validation()
