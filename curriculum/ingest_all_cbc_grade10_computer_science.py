"""
VLearn CBC Grade 10 Computer Science — Master Ingestion Engine
Executes complete ingestion and enrichment for Topics 1, 2, 3, and 4.
"""

import os
import sys
import time
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.ingest_cbc_grade10_computer_science_topic1 import ingest_grade10_topic1
from curriculum.ingest_cbc_grade10_computer_science_topic2 import ingest_grade10_topic2
from curriculum.ingest_cbc_grade10_computer_science_topic3 import ingest_grade10_topic3
from curriculum.ingest_cbc_grade10_computer_science_topic4 import ingest_grade10_topic4
from curriculum.ingest_cbc_grade10_computer_science_topic5 import ingest_grade10_topic5
from curriculum.ingest_cbc_grade10_computer_science_topic6 import ingest_grade10_topic6

def run_master_ingestion():
    start_time = time.time()
    print("=" * 80)
    print("STARTING CBC GRADE 10 COMPUTER SCIENCE MASTER INGESTION (TOPICS 1-6)")
    print("=" * 80)

    ingest_grade10_topic1(replace=True)
    print("\n")
    ingest_grade10_topic2(replace=True)
    print("\n")
    ingest_grade10_topic3(replace=True)
    print("\n")
    ingest_grade10_topic4(replace=True)
    print("\n")
    ingest_grade10_topic5(replace=True)
    print("\n")
    ingest_grade10_topic6(replace=True)

    duration = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"MASTER INGESTION COMPLETED IN {duration:.2f} SECONDS")
    print("=" * 80)

if __name__ == "__main__":
    run_master_ingestion()
