"""
Script to apply comprehensive pedagogical upgrades to Topic 8, Topic 9, and Topic 10.
Adds:
1. learning_goal on Page 1 of every lesson.
2. deep concept_explanation with analogies.
3. step-by-step worked_example on every lesson.
4. key_takeaway summary card on every lesson.
5. 4 valid MCQs with 4 options, clear answers, and explanations.
6. Zero citation leaks.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.ingest_cbc_grade10_computer_science_topic8 import ingest_grade10_topic8
from curriculum.ingest_cbc_grade10_computer_science_topic9 import ingest_grade10_topic9
from curriculum.ingest_cbc_grade10_computer_science_topic10 import ingest_grade10_topic10

print("Imported ingestion modules successfully.")
