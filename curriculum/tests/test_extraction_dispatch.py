"""
curriculum/tests/test_extraction_dispatch.py

Tests for KnowledgePack pipeline dispatching, timing logs, and fallback failure persistence:
1. dispatch_knowledge_pack_pipeline records dispatch duration in logs
2. Synchronous fallback path sets KnowledgePack.status = 'failed' on unhandled exception
3. Fallback path duration is logged
"""

import time
from unittest.mock import patch, MagicMock
from django.test import TransactionTestCase, override_settings
from django.db import transaction

from curriculum.models import Curriculum, Grade, Subject, KnowledgePack
from curriculum.tasks import dispatch_knowledge_pack_pipeline


class ExtractionDispatchPipelineTests(TransactionTestCase):
    def setUp(self):
        self.curriculum = Curriculum.objects.create(name="National Curriculum")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 3", level=3)
        self.subject = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.kp = KnowledgePack.objects.create(
            subject=self.subject,
            source_file_url="https://example.com/chemistry.pdf",
            status="processing",
        )

    def test_dispatch_records_duration_in_logs(self):
        """Verify that successful Celery dispatch records duration in logs."""
        with override_settings(CELERY_TASK_ALWAYS_EAGER=False):
            with patch("curriculum.tasks.process_textbook_pipeline_task.delay") as mock_delay:
                with self.assertLogs("curriculum", level="INFO") as cm:
                    with transaction.atomic():
                        dispatch_knowledge_pack_pipeline(self.kp.id)

                    mock_delay.assert_called_once_with(self.kp.id)
                    log_output = " ".join(cm.output)
                    self.assertIn("Celery dispatch handoff succeeded in", log_output)
                    self.assertIn(f"[KP {self.kp.id}]", log_output)

    def test_fallback_runner_persists_failure_status(self):
        """Verify that an unhandled exception in fallback runner sets KnowledgePack.status = 'failed'."""
        with override_settings(CELERY_TASK_ALWAYS_EAGER=False):
            # Celery dispatch fails, triggering fallback
            with patch(
                "curriculum.tasks.process_textbook_pipeline_task.delay",
                side_effect=Exception("Redis connection refused")
            ):
                # Fallback task execution also raises error
                with patch(
                    "curriculum.tasks.process_textbook_pipeline_task.apply",
                    side_effect=RuntimeError("OCR segmentation fault")
                ):
                    with self.assertLogs("curriculum", level="ERROR") as cm:
                        with transaction.atomic():
                            dispatch_knowledge_pack_pipeline(self.kp.id)
                        # Allow daemon thread a moment to finish
                        time.sleep(0.5)

                        self.kp.refresh_from_db()
                        self.assertEqual(self.kp.status, "failed")
                        log_output = " ".join(cm.output)
                        self.assertIn("Error in fallback KP pipeline thread after", log_output)

    def test_fallback_runner_duration_is_logged_on_success(self):
        """Verify fallback thread logs execution duration on successful completion."""
        with override_settings(CELERY_TASK_ALWAYS_EAGER=False):
            with patch(
                "curriculum.tasks.process_textbook_pipeline_task.delay",
                side_effect=Exception("Redis connection refused")
            ):
                with patch("curriculum.tasks.process_textbook_pipeline_task.apply") as mock_apply:
                    with self.assertLogs("curriculum", level="INFO") as cm:
                        with transaction.atomic():
                            dispatch_knowledge_pack_pipeline(self.kp.id)
                        time.sleep(0.5)

                        mock_apply.assert_called_once_with(args=[self.kp.id])
                        log_output = " ".join(cm.output)
                        self.assertIn("Fallback thread completed successfully in", log_output)
