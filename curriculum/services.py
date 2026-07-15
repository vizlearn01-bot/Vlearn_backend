import json
import uuid

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
        # In a real implementation, this would call the Gemini API.
        # Prompt: "Generate a lesson outline for {grade_name} {subject_name} on {topic_name}..."
        
        # Mocking the AI response for now:
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
        # In a real implementation, this would call the Gemini API.
        # Prompt: "Generate the {block_type} section titled {title} for topic {topic_name}..."

        return f"**Generated {title}**\n\nThis is AI generated placeholder text for the `{block_type}` block in `{topic_name}`. \n\n* Previous Context length: {len(previous_context)}"
