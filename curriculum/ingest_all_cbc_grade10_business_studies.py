"""
VLearn CBC Grade 10 Business Studies — Master Ingestion Orchestrator
Ingests and enriches all topics for Grade 10 Business Studies in sequential order.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.ingest_cbc_grade10_business_studies_topic1 import ingest_grade10_business_studies_topic1
from curriculum.ingest_cbc_grade10_business_studies_topic2 import ingest_grade10_business_studies_topic2
from curriculum.ingest_cbc_grade10_business_studies_topic3 import ingest_grade10_business_studies_topic3
from curriculum.ingest_cbc_grade10_business_studies_topic4 import ingest_grade10_business_studies_topic4
from curriculum.ingest_cbc_grade10_business_studies_topic5 import ingest_grade10_business_studies_topic5
from curriculum.ingest_cbc_grade10_business_studies_topic6 import ingest_grade10_business_studies_topic6
from curriculum.ingest_cbc_grade10_business_studies_topic7 import ingest_grade10_business_studies_topic7
from curriculum.ingest_cbc_grade10_business_studies_topic8 import ingest_grade10_business_studies_topic8

def ingest_all():
    print("*" * 80)
    print("VLEARN CBC GRADE 10 BUSINESS STUDIES — MASTER INGESTION PIPELINE")
    print("*" * 80)

    ingest_grade10_business_studies_topic1(replace=True)
    ingest_grade10_business_studies_topic2(replace=True)
    ingest_grade10_business_studies_topic3(replace=True)
    ingest_grade10_business_studies_topic4(replace=True)
    ingest_grade10_business_studies_topic5(replace=True)
    ingest_grade10_business_studies_topic6(replace=True)
    ingest_grade10_business_studies_topic7(replace=True)
    ingest_grade10_business_studies_topic8(replace=True)

    print("*" * 80)
    print("MASTER INGESTION PIPELINE COMPLETED SUCCESSFULLY!")
    print("*" * 80)

if __name__ == "__main__":
    ingest_all()
