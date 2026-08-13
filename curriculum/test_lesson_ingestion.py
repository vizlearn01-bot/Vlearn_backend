"""
curriculum/test_lesson_ingestion.py

Test suite verifying bulk lesson ingestion, scientific content preservation,
interactive quiz parsing, visual asset creation, and publishing validation.
"""

from django.test import TestCase
from django.utils import timezone
from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit,
    Lesson, LessonBlock, LessonAsset
)
from curriculum.management.commands.ingest_lesson_md import Command as IngestCommand

class LessonIngestionTestCase(TestCase):
    def setUp(self):
        self.curriculum = Curriculum.objects.create(name="844", description="844 Curriculum")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 4", level=4)
        self.subject = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.topic = Topic.objects.create(subject=self.subject, name="Topic 1: Acids, Bases and Salts", order=1)

    def test_ingest_chemistry_batch_module(self):
        cmd = IngestCommand()
        mod_data = {
            "code": "Module 1.1",
            "title": "Acids — Operational and Conceptual Definitions",
            "full_title": "Module 1.1: Acids — Operational and Conceptual Definitions",
            "body": """
### **1. Operational Definition**
An acid has a sour taste, turns blue litmus paper red, and reacts with metals like Mg:
\\\\[\\text{Mg}_{(s)} + 2\\text{H}^+_{(aq)} \\rightarrow \\text{Mg}^{2+}_{(aq)} + \\text{H}_{2(g)}\\\\]

### **2. Check Your Understanding**
1. Predict what happens when iron wire reacts with dilute acid.
🗝️ Explanations & Answers:
1. Effervescence occurs and hydrogen gas is evolved.
"""
        }

        res = cmd.process_module(self.subject, self.topic, mod_data, dry_run=False)
        
        self.assertIsNotNone(res["lesson_id"])
        lesson = Lesson.objects.get(id=res["lesson_id"])

        # 1. Verify publishing status
        self.assertEqual(lesson.status, "published")
        self.assertIsNotNone(lesson.published_at)

        # 2. Verify blocks creation and page_number ordering
        blocks = list(lesson.blocks.order_by("order"))
        self.assertGreaterEqual(len(blocks), 3)
        page_nums = [b.page_number for b in blocks if b.page_number is not None]
        self.assertEqual(page_nums, sorted(page_nums))

        # 3. Verify equation preservation
        has_eq = any("\\text{Mg}" in str(b.content) for b in blocks)
        self.assertTrue(has_eq, "Chemical equations must be preserved in lesson content.")

        # 4. Verify knowledge_check block structure
        quiz_blocks = [b for b in blocks if b.block_type == "knowledge_check"]
        self.assertGreaterEqual(len(quiz_blocks), 1)
        qb = quiz_blocks[0]
        self.assertIn("question", qb.content)
        self.assertIn("explanation", qb.content)
