"""
VLearn CBC Grade 10 Business Studies — Master QA Test Runner
Executes comprehensive automated integrity verification test suites across ALL 15 topics.
"""

import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")

from curriculum.test_cbc_grade10_business_studies_topic1 import TestCBCGrade10BusinessStudiesTopic1
from curriculum.test_cbc_grade10_business_studies_topic2 import TestCBCGrade10BusinessStudiesTopic2
from curriculum.test_cbc_grade10_business_studies_topic3 import TestCBCGrade10BusinessStudiesTopic3
from curriculum.test_cbc_grade10_business_studies_topic4 import TestCBCGrade10BusinessStudiesTopic4
from curriculum.test_cbc_grade10_business_studies_topic5 import TestCBCGrade10BusinessStudiesTopic5
from curriculum.test_cbc_grade10_business_studies_topic6 import TestCBCGrade10BusinessStudiesTopic6
from curriculum.test_cbc_grade10_business_studies_topic7 import TestCBCGrade10BusinessStudiesTopic7
from curriculum.test_cbc_grade10_business_studies_topic8 import TestCBCGrade10BusinessStudiesTopic8
from curriculum.test_cbc_grade10_business_studies_topic9 import TestCBCGrade10BusinessStudiesTopic9
from curriculum.test_cbc_grade10_business_studies_topic10 import TestCBCGrade10BusinessStudiesTopic10
from curriculum.test_cbc_grade10_business_studies_topic11 import TestCBCGrade10BusinessStudiesTopic11
from curriculum.test_cbc_grade10_business_studies_topic12 import TestCBCGrade10BusinessStudiesTopic12
from curriculum.test_cbc_grade10_business_studies_topic13 import TestCBCGrade10BusinessStudiesTopic13
from curriculum.test_cbc_grade10_business_studies_topic14 import TestCBCGrade10BusinessStudiesTopic14
from curriculum.test_cbc_grade10_business_studies_topic15 import TestCBCGrade10BusinessStudiesTopic15

def suite():
    s = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    test_classes = [
        TestCBCGrade10BusinessStudiesTopic1,
        TestCBCGrade10BusinessStudiesTopic2,
        TestCBCGrade10BusinessStudiesTopic3,
        TestCBCGrade10BusinessStudiesTopic4,
        TestCBCGrade10BusinessStudiesTopic5,
        TestCBCGrade10BusinessStudiesTopic6,
        TestCBCGrade10BusinessStudiesTopic7,
        TestCBCGrade10BusinessStudiesTopic8,
        TestCBCGrade10BusinessStudiesTopic9,
        TestCBCGrade10BusinessStudiesTopic10,
        TestCBCGrade10BusinessStudiesTopic11,
        TestCBCGrade10BusinessStudiesTopic12,
        TestCBCGrade10BusinessStudiesTopic13,
        TestCBCGrade10BusinessStudiesTopic14,
        TestCBCGrade10BusinessStudiesTopic15,
    ]
    
    for tc in test_classes:
        s.addTests(loader.loadTestsFromTestCase(tc))
    return s

if __name__ == "__main__":
    print("=" * 80)
    print("VLEARN CBC GRADE 10 BUSINESS STUDIES — COMPLETE 15-TOPIC MASTER QA RUNNER")
    print("=" * 80)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    
    if result.wasSuccessful():
        print("=" * 80)
        print("ALL 15 GRADE 10 BUSINESS STUDIES TOPICS PASSED WITH 100% SUCCESS!")
        print("=" * 80)
        sys.exit(0)
    else:
        print("=" * 80)
        print(f"FAILED: {len(result.failures)} failures, {len(result.errors)} errors")
        print("=" * 80)
        sys.exit(1)
