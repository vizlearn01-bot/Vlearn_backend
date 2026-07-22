from django.test import TestCase
from curriculum.generation.optimizer.models import ValidationReport, QualityScore
from curriculum.generation.optimizer.quality import QualityEngine
from curriculum.generation.optimizer.validator import CompilerValidator
from curriculum.generation.planner.models import LearningExperiencePlan, StrategyNode, InstructionalIntent, PersonalizationOptions

class OptimizerTests(TestCase):
    
    def setUp(self):
        self.mock_intent = InstructionalIntent(
            learning_moment="Introduce testing",
            required_cognitive_change="Understand tests",
            student_goal="Write a test"
        )
        self.mock_personalization = PersonalizationOptions(
            remediation_available=True,
            adaptive_questioning=True,
            difficulty_adjustment=True
        )
        self.valid_node1 = StrategyNode(
            node_id="node_1",
            node_type="concept",
            instructional_intent=self.mock_intent,
            content="This is a test concept.",
            personalization=self.mock_personalization,
            next_nodes=["node_2"]
        )
        self.valid_node2 = StrategyNode(
            node_id="node_2",
            node_type="assessment",
            instructional_intent=self.mock_intent,
            content="Question?",
            personalization=self.mock_personalization,
            next_nodes=[]
        )
        self.valid_plan = LearningExperiencePlan(
            plan_id="plan_1",
            subject="Test",
            title="Test Plan",
            entry_node_id="node_1",
            nodes=[self.valid_node1, self.valid_node2]
        )

    def test_pedagogical_validation_passes_valid_plan(self):
        report = CompilerValidator.validate_plan(self.valid_plan)
        self.assertFalse(report.has_errors)
        
        ok_checks = [c.label for c in report.checks if c.severity == 'ok']
        self.assertIn("Structural Integrity", ok_checks)
        self.assertIn("Assessment Coverage", ok_checks)
        self.assertIn("Remediation Paths", ok_checks)

    def test_pedagogical_validation_fails_empty_plan(self):
        empty_plan = LearningExperiencePlan(
            plan_id="plan_1",
            subject="Test",
            title="Empty Plan",
            entry_node_id="none",
            nodes=[]
        )
        report = CompilerValidator.validate_plan(empty_plan)
        self.assertTrue(report.has_errors)

    def test_quality_engine_deterministic_score(self):
        score_report = QualityEngine.calculate_score(self.valid_plan)
        # Interaction ratio = 1/2 = 0.5 (Between 0.2 and 0.6 is ideal)
        # Remediation present
        # No heavy nodes
        # No branching missing criteria (no branches)
        self.assertEqual(score_report.score, 100)
        self.assertEqual(score_report.metrics['interaction_ratio'], 0.5)

    def test_quality_engine_penalizes_low_interaction(self):
        node3 = StrategyNode(
            node_id="node_3",
            node_type="concept",
            instructional_intent=self.mock_intent,
            content="More reading.",
            personalization=self.mock_personalization,
            next_nodes=[]
        )
        self.valid_node1.next_nodes = ["node_3"]
        self.valid_plan.nodes = [self.valid_node1, node3]
        
        score_report = QualityEngine.calculate_score(self.valid_plan)
        # 0 assessments out of 2 nodes = 0.0 interaction ratio
        self.assertTrue(score_report.score < 100)
        self.assertIn('interaction_penalty', score_report.metrics)
