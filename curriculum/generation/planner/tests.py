import unittest

from curriculum.generation.planner.models import LearningExperiencePlan
from curriculum.generation.planner.graph_validator import GraphValidator

class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.valid_plan = {
            "title": "Test Plan",
            "cognitive_analysis": {"difficulty": "medium"},
            "strategy_selected": "Predict-Observe",
            "entry_node_id": "hook_1",
            "nodes": [
                {
                    "node_id": "hook_1",
                    "node_type": "predict",
                    "instructional_intent": {
                        "learning_moment": "Start",
                        "student_goal": "Guess",
                        "required_cognitive_change": "From blank to curious",
                        "evidence_of_understanding": "Makes a guess",
                        "recommended_learning_support": "Ask a question"
                    },
                    "personalization": {
                        "extension_available": False,
                        "remediation_available": False,
                        "adaptive_questioning": False
                    },
                    "content": "What happens if we drop a feather?",
                    "next_nodes": ["observe_1"]
                },
                {
                    "node_id": "observe_1",
                    "node_type": "observe",
                    "instructional_intent": {
                        "learning_moment": "Show",
                        "student_goal": "Watch",
                        "required_cognitive_change": "Notice it falls slowly",
                        "evidence_of_understanding": "States it falls slowly",
                        "recommended_learning_support": "Show it falling"
                    },
                    "personalization": {
                        "extension_available": False,
                        "remediation_available": False,
                        "adaptive_questioning": False
                    },
                    "content": "It falls slowly.",
                    "next_nodes": []
                }
            ]
        }

    def test_valid_schema(self):
        plan = LearningExperiencePlan(**self.valid_plan)
        self.assertEqual(plan.title, "Test Plan")

    def test_graph_validator_valid(self):
        errors = GraphValidator.validate(self.valid_plan)
        self.assertEqual(len(errors), 0)

    def test_graph_validator_orphan(self):
        orphan_node = self.valid_plan["nodes"][1].copy()
        orphan_node["node_id"] = "orphan_1"
        orphan_node["next_nodes"] = []
        self.valid_plan["nodes"].append(orphan_node)
        
        errors = GraphValidator.validate(self.valid_plan)
        self.assertEqual(len(errors), 1)
        self.assertIn("Orphan nodes detected", errors[0])

    def test_graph_validator_invalid_branching(self):
        # branching node without criteria
        self.valid_plan["nodes"][0]["next_nodes"] = ["observe_1", "observe_2"]
        # add observe_2 to prevent non-existent reference
        obs_2 = self.valid_plan["nodes"][1].copy()
        obs_2["node_id"] = "observe_2"
        self.valid_plan["nodes"].append(obs_2)
        
        errors = GraphValidator.validate(self.valid_plan)
        self.assertEqual(len(errors), 1)
        self.assertIn("branches to 2 nodes but lacks", errors[0])

from curriculum.generation.intelligence.selection import FrameworkSelectionEngine
from curriculum.models import Concept, LearningUnit, Topic, Subject, Grade, Curriculum
from django.test import TestCase

class FrameworkSelectionTests(TestCase):
    def setUp(self):
        curriculum = Curriculum.objects.create(name="Test Curriculum")
        grade = Grade.objects.create(curriculum=curriculum, name="Test Grade", level=1)
        subject = Subject.objects.create(grade=grade, name="Test Subject")
        topic = Topic.objects.create(subject=subject, name="Test Topic", order=1)
        self.lu = LearningUnit.objects.create(topic=topic, name="Test Unit", order=1)

    def test_generic_fallback(self):
        # No concepts, should return generic_fallback
        result = FrameworkSelectionEngine.select(self.lu)
        self.assertEqual(result["framework_id"], "generic_fallback")

    def test_math_heavy_selection(self):
        Concept.objects.create(
            name="Quadratic Equation",
            learning_unit=self.lu,
            instructional_metadata={"cognitive_category": "mathematical_reasoning"}
        )
        result = FrameworkSelectionEngine.select(self.lu)
        self.assertEqual(result["framework_id"], "abstract_logical")

    def test_procedural_selection(self):
        Concept.objects.create(
            name="Long Division",
            learning_unit=self.lu,
            instructional_metadata={"procedural_nature": True}
        )
        result = FrameworkSelectionEngine.select(self.lu)
        self.assertEqual(result["framework_id"], "procedural_algorithmic")

    def test_discussion_heavy_selection(self):
        Concept.objects.create(
            name="Ethics of AI",
            learning_unit=self.lu,
            instructional_metadata={"discussion_suitability": True}
        )
        result = FrameworkSelectionEngine.select(self.lu)
        self.assertEqual(result["framework_id"], "human_social")

    def test_process_based_selection(self):
        Concept.objects.create(
            name="Photosynthesis",
            learning_unit=self.lu,
            instructional_metadata={"experimentation_suitability": True}
        )
        result = FrameworkSelectionEngine.select(self.lu)
        self.assertEqual(result["framework_id"], "process_based")

    def test_keyword_fallback_selection(self):
        Concept.objects.create(
            name="Chemical Reaction",
            learning_unit=self.lu,
            keywords=["process", "mechanism"],
            instructional_metadata={} # Missing metadata
        )
        result = FrameworkSelectionEngine.select(self.lu)
        self.assertEqual(result["framework_id"], "process_based")
