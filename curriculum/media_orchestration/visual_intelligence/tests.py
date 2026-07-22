import unittest
from .models import VisualSpecification
from .renderer import VisualRenderer

class VisualIntelligenceTests(unittest.TestCase):
    def test_renderer_valid_svg(self):
        spec = VisualSpecification(
            node_id="test_node_1",
            format="svg",
            code='<svg width="100" height="100"><circle cx="50" cy="50" r="40" /></svg>',
            explanation="A simple circle.",
            alt_text="Circle"
        )
        visual, failure = VisualRenderer.render(spec)
        self.assertIsNotNone(visual)
        self.assertIsNone(failure)
        self.assertEqual(visual.render_format, "svg")
        self.assertEqual(visual.raw_code, '<svg width="100" height="100"><circle cx="50" cy="50" r="40" /></svg>')
        
    def test_renderer_invalid_svg(self):
        spec = VisualSpecification(
            node_id="test_node_2",
            format="svg",
            code='<g><circle cx="50" cy="50" r="40" /></g>', # missing <svg> tags
            explanation="A simple circle.",
            alt_text="Circle"
        )
        visual, failure = VisualRenderer.render(spec)
        self.assertIsNone(visual)
        self.assertIsNotNone(failure)
        self.assertIn("malformed", failure.reason)
        
    def test_renderer_valid_mermaid(self):
        spec = VisualSpecification(
            node_id="test_node_3",
            format="mermaid",
            code='```mermaid\ngraph TD\n  A-->B\n```', # Mocking the common LLM markdown leak
            explanation="A simple flowchart.",
            alt_text="Flowchart"
        )
        visual, failure = VisualRenderer.render(spec)
        self.assertIsNotNone(visual)
        self.assertIsNone(failure)
        self.assertEqual(visual.render_format, "mermaid")
        self.assertEqual(visual.raw_code, "graph TD\n  A-->B")
        
    def test_renderer_unsupported_format(self):
        spec = VisualSpecification(
            node_id="test_node_4",
            format="unknown_format",
            code='some code',
            explanation="Some explanation.",
            alt_text="Unknown"
        )
        visual, failure = VisualRenderer.render(spec)
        self.assertIsNone(visual)
        self.assertIsNotNone(failure)
        self.assertIn("Unsupported", failure.reason)
