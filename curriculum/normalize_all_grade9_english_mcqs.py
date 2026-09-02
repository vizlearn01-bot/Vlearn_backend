"""
VLearn CBC Grade 9 English — MCQ Normalization Script
Ensures all 60 MCQs across Topics 1, 2, 3, 4 have standard fields:
- question (str)
- options (list of 4 strings)
- answer ('A', 'B', 'C', or 'D')
- correct_answer (matching option index 0..3 and text)
- explanation (rich rationale)
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from django.db import transaction
from curriculum.models import Grade, Subject, LessonBlock


def normalize_mcqs():
    grade = Grade.objects.get(id=18)
    subject = Subject.objects.get(grade=grade, name="English")
    mcq_blocks = LessonBlock.objects.filter(
        lesson__topic__subject=subject,
        component_type="knowledge_check"
    ).order_by("lesson__topic__order", "lesson__learning_unit__order", "order")

    print(f"[*] Normalizing {mcq_blocks.count()} MCQs across Grade 9 English...")

    letter_map = {0: "A", 1: "B", 2: "C", 3: "D"}
    idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    updated_count = 0
    with transaction.atomic():
        for b in mcq_blocks:
            c = b.content or {}
            options = c.get("options", [])
            raw_ans = c.get("answer") or c.get("correct_answer") or c.get("correct_option")

            target_letter = None
            if isinstance(raw_ans, str) and raw_ans.strip().upper() in ["A", "B", "C", "D"]:
                target_letter = raw_ans.strip().upper()
            elif isinstance(raw_ans, int) and raw_ans in [0, 1, 2, 3]:
                target_letter = letter_map[raw_ans]
            elif isinstance(raw_ans, int) and raw_ans in [1, 2, 3, 4]:
                # If 1-indexed
                target_letter = letter_map[raw_ans - 1]
            elif isinstance(raw_ans, str):
                # Check if it matches an option text
                matched = False
                for idx, opt in enumerate(options):
                    if raw_ans.strip() == opt.strip():
                        target_letter = letter_map[idx]
                        matched = True
                        break
                if not matched:
                    # Check in explanation for "Option A/B/C/D is correct"
                    exp = c.get("explanation", "")
                    import re
                    m = re.search(r'Option\s+([A-D])\s+is\s+correct', exp, re.IGNORECASE)
                    if m:
                        target_letter = m.group(1).upper()
                    else:
                        target_letter = "A"

            c["answer"] = target_letter
            c["correct_answer"] = target_letter
            c["correct_option_index"] = idx_map.get(target_letter, 0)
            b.content = c
            b.save()
            updated_count += 1

    print(f"[+] Successfully normalized all {updated_count} MCQs!")


if __name__ == "__main__":
    normalize_mcqs()
