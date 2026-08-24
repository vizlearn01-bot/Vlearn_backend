import libcst as cst
from libcst.metadata import PositionProvider

class RewriteVisitor(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def __init__(self, topic, img_assignments):
        self.topic = topic
        self.img_assignments = img_assignments
        self.current_lesson = None

    def visit_AssignTarget(self, node: cst.AssignTarget) -> bool:
        if isinstance(node.target, cst.Name) and node.target.value.startswith("LESSON_"):
            self.current_lesson = int(node.target.value.split('_')[1])
        return True

    # But we want to modify Dicts...
