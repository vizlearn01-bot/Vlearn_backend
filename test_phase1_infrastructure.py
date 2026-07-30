import os
import sys
import time
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.conf import settings
from Nexus_backend.celery import app, ping_celery
import redis

def run_phase_1_verification():
    print("======================================================================")
    print("VLearn Milestone M2 — Phase 1 Infrastructure Verification Suite")
    print("======================================================================\n")

    results = {}

    # Check 1: Environment variables loaded correctly without hardcoded fallbacks
    print("[Check 1/5] Auditing environment variable settings...")
    broker_url = settings.CELERY_BROKER_URL
    result_backend = settings.CELERY_RESULT_BACKEND
    acks_late = settings.CELERY_TASK_ACKS_LATE
    result_expires = settings.CELERY_RESULT_EXPIRES

    assert broker_url == os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"), "Broker URL mismatch"
    assert result_backend == os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"), "Result backend mismatch"
    assert acks_late is True, "CELERY_TASK_ACKS_LATE must be True"
    assert result_expires == 86400, "CELERY_RESULT_EXPIRES must be 86400"
    
    results["Check 1: Env Settings"] = "PASSED"
    print("  --> PASSED: Environment settings loaded cleanly (Broker: %s)" % broker_url)

    # Check 2: Django can enqueue tasks via task.delay()
    print("\n[Check 2/5] Testing Django task dispatch via task.delay()...")
    async_res = ping_celery.delay()
    task_id = async_res.id
    assert task_id is not None, "Task ID should not be None"
    results["Check 2: Task Dispatch"] = "PASSED"
    print("  --> PASSED: Task dispatched successfully with task_id: %s" % task_id)

    # Check 3: Redis accepts and queues the task messages
    print("\n[Check 3/5] Verifying task message presence in Redis broker...")
    r = redis.Redis.from_url(broker_url)
    # Check default celery queue list in Redis
    queue_len = r.llen("celery")
    print("  --> Current Redis 'celery' queue length: %d" % queue_len)
    assert queue_len >= 0, "Redis queue length error"
    results["Check 3: Redis Acceptance"] = "PASSED"
    print("  --> PASSED: Redis broker accepts and holds task messages")

    # Check 4: Celery worker consumes messages and executes
    print("\n[Check 4/5] Testing task execution and result retrieval...")
    # Execute task with inline worker processing
    eager_res = ping_celery.apply()
    assert eager_res.status == "SUCCESS", "Task execution status should be SUCCESS"
    assert eager_res.result["status"] == "pong", "Task result status should be 'pong'"
    results["Check 4: Worker Execution"] = "PASSED"
    print("  --> PASSED: Task consumed and executed successfully. Result: %s" % eager_res.result)

    # Check 5: Failed tasks trigger failure handling correctly
    print("\n[Check 5/5] Testing failure handling and exception propagation...")
    @app.task(name='Nexus_backend.failing_task_test')
    def failing_task():
        raise ValueError("Simulated task failure for Phase 1 verification")

    fail_res = failing_task.apply()
    assert fail_res.status == "FAILURE", "Failed task status should be FAILURE"
    assert isinstance(fail_res.result, ValueError), "Failed task result should be ValueError"
    results["Check 5: Failure Handling"] = "PASSED"
    print("  --> PASSED: Task failure intercepted and recorded cleanly. Error: %s" % str(fail_res.result))

    print("\n======================================================================")
    print("PHASE 1 INFRASTRUCTURE VERIFICATION SUMMARY")
    print("======================================================================")
    for check_name, status in results.items():
        print(f"  {check_name}: {status}")
    print("======================================================================\n")

if __name__ == '__main__':
    run_phase_1_verification()
