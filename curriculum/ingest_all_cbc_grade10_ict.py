"""
Master Ingestion Orchestrator for VLearn CBC Grade 10 ICT (All 9 Topics)
Runs all 9 topic ingestion modules in sequence with full transaction safety.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.ingest_cbc_grade10_ict_topic1 import ingest_grade10_ict_topic1
from curriculum.ingest_cbc_grade10_ict_topic2 import ingest_grade10_ict_topic2
from curriculum.ingest_cbc_grade10_ict_topic3 import ingest_grade10_ict_topic3
from curriculum.ingest_cbc_grade10_ict_topic4 import ingest_grade10_ict_topic4
from curriculum.ingest_cbc_grade10_ict_topic5 import ingest_grade10_ict_topic5
from curriculum.ingest_cbc_grade10_ict_topic6 import ingest_grade10_ict_topic6
from curriculum.ingest_cbc_grade10_ict_topic7 import ingest_grade10_ict_topic7
from curriculum.ingest_cbc_grade10_ict_topic8 import ingest_grade10_ict_topic8
from curriculum.ingest_cbc_grade10_ict_topic9 import ingest_grade10_ict_topic9

def ingest_all_grade10_ict(replace=True):
    print("=" * 80)
    print("MASTER INGESTION: GRADE 10 ICT (ALL 9 TOPICS)")
    print("=" * 80)
    
    ingest_grade10_ict_topic1(replace=replace)
    ingest_grade10_ict_topic2(replace=replace)
    ingest_grade10_ict_topic3(replace=replace)
    ingest_grade10_ict_topic4(replace=replace)
    ingest_grade10_ict_topic5(replace=replace)
    ingest_grade10_ict_topic6(replace=replace)
    ingest_grade10_ict_topic7(replace=replace)
    ingest_grade10_ict_topic8(replace=replace)
    ingest_grade10_ict_topic9(replace=replace)
    
    print("\n" + "=" * 80)
    print("ALL 9 GRADE 10 ICT TOPICS INGESTED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    ingest_all_grade10_ict(replace=True)
