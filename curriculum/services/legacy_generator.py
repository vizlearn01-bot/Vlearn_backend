class LessonGeneratorService:
    """
    Service responsible for interacting with the AI model to generate
    lesson outlines and individual blocks.
    """

    @staticmethod
    def generate_outline(topic_name, subject_name, grade_name):
        """
        Generates a structured outline (list of blocks) for a topic.
        Returns a list of dicts: [{"title": "...", "block_type": "..."}]
        """
        return [
            {"title": "Objectives", "block_type": "objective"},
            {"title": "Introduction to " + topic_name, "block_type": "overview"},
            {"title": "Core Concepts", "block_type": "core_explanation"},
            {"title": "Worked Example", "block_type": "example"},
            {"title": "Summary", "block_type": "summary"},
        ]

    @staticmethod
    def generate_block_content(topic_name, block_type, title, previous_context=""):
        """
        Generates the detailed markdown content for a specific block.
        """
        return (
            f"**Generated {title}**\n\n"
            f"This is AI generated placeholder text for the `{block_type}` block in `{topic_name}`. \n\n"
            f"* Previous Context length: {len(previous_context)}"
        )
