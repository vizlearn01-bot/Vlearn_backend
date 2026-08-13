"""
VLearn Form 4 Physics — Topic 1 Validation Test Suite
Audits curriculum hierarchy, lesson completeness, sequential page numbering,
KaTeX LaTeX delimiter balance, developer terminology leak prevention,
worked example structures, and knowledge check completeness.

Run with pytest:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/pytest curriculum/test_form4_physics_ingestion.py -v

Or run directly:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/test_form4_physics_ingestion.py
"""

import os
import sys
import re
import pytest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

DEVELOPER_LEAK_PATTERNS = [
    r"\bcomponent_type\b",
    r"\bblock_type\b",
    r"\bai_instruction\b",
    r"\basset_info\b",
    r"\bblock_id\b",
    r"\bTODO\b",
    r"\bDEBUG\b",
    r"\braw_prompt\b",
    r"Visual Representation:",
    r"Building Intuition:",
    r"Enrichment Slot",
    r"AI-generated visual",
]

def get_physics_topic():
    return Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Thin Lenses"
    ).first()

def extract_all_text(content):
    """Recursively extract all text from content objects."""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        return " ".join(extract_all_text(x) for x in content)
    elif isinstance(content, dict):
        return " ".join(extract_all_text(v) for v in content.values())
    return ""

def check_latex_balance(text):
    """Verify that $ and $$ delimiters are balanced."""
    issues = []
    # Count display math $$
    display_count = len(re.findall(r"\$\$", text))
    if display_count % 2 != 0:
        issues.append(f"Odd number of $$ delimiters ({display_count})")

    # Remove $$ blocks, then count inline $
    cleaned = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    inline_count = len(re.findall(r"(?<!\\)\$", cleaned))
    if inline_count % 2 != 0:
        issues.append(f"Odd number of inline $ delimiters ({inline_count})")

    return issues


# =============================================================================
# TEST CASES
# =============================================================================

class TestPhysicsTopic1Ingestion:

    def test_curriculum_hierarchy_exists(self):
        subject = Subject.objects.filter(grade__name="Form 4", name="Physics").first()
        assert subject is not None, "Form 4 Physics subject must exist"
        
        topic = get_physics_topic()
        assert topic is not None, "Topic 1: Thin Lenses must exist"
        assert topic.order == 1
        
        units = topic.learning_units.all().order_by("order")
        assert units.count() == 3, f"Expected 3 Learning Units in Topic 1, found {units.count()}"

    def test_lessons_published_and_complete(self):
        topic = get_physics_topic()
        assert topic is not None
        
        units = topic.learning_units.all().order_by("order")
        for unit in units:
            lesson = unit.lessons.first()
            assert lesson is not None, f"LearningUnit '{unit.name}' must have an associated Lesson"
            assert lesson.status == "published", f"Lesson '{lesson.title}' must be published"
            assert lesson.blocks.count() >= 14, f"Lesson '{lesson.title}' should have at least 14 blocks"

    def test_sequential_page_numbers(self):
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            blocks = lesson.blocks.all().order_by("order")
            pages = [b.page_number for b in blocks if b.page_number is not None]
            assert len(pages) > 0, f"Lesson '{lesson.title}' has no numbered pages"
            
            distinct_pages = sorted(list(set(pages)))
            assert distinct_pages[0] == 1, f"First page must be 1 in '{lesson.title}'"
            
            # Check sequential with no gaps
            for idx, p in enumerate(distinct_pages):
                assert p == idx + 1, f"Page numbers must be sequential without gaps in '{lesson.title}' (found {p} at index {idx})"

    def test_valid_block_types_and_components(self):
        valid_block_types = {
            'learning_goal', 'concept_explanation', 'formula_breakdown',
            'worked_example', 'step_process', 'comparison_table',
            'definition_card', 'suggested_diagram', 'suggested_graph',
            'suggested_simulation', 'suggested_image', 'prediction', 'reflection',
            'common_misconception', 'common_mistake', 'callout',
            'knowledge_check', 'summary', 'key_takeaway'
        }
        
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                assert block.block_type in valid_block_types, (
                    f"Invalid block_type '{block.block_type}' in block ID {block.id} ('{lesson.title}')"
                )
                assert block.page_title, f"Block ID {block.id} must have a page_title"
                assert block.content, f"Block ID {block.id} must have non-empty content"

    def test_visual_assets_enrichment_complete(self):
        topic = get_physics_topic()
        assert topic is not None

        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            svg_assets = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram", source_type="ai_generated")
            assert svg_assets.count() >= 3, f"Lesson '{lesson.title}' should have enriched SVG assets"
            
            # Check each SVG asset has valid svg_content in metadata
            for asset in svg_assets:
                assert asset.metadata and "svg_content" in asset.metadata, f"Asset {asset.id} missing svg_content"
                assert "<svg" in asset.metadata["svg_content"], f"Asset {asset.id} svg_content must contain SVG XML"

            # Check Wikimedia photographic assets
            wikimedia_assets = LessonAsset.objects.filter(lesson=lesson, asset_type="image", source_type="external")
            assert wikimedia_assets.count() >= 1, f"Lesson '{lesson.title}' should have at least 1 Wikimedia asset"
            for w_asset in wikimedia_assets:
                assert w_asset.url.startswith("https://upload.wikimedia.org"), f"Asset {w_asset.id} must have valid Wikimedia URL"
                assert w_asset.metadata and "author" in w_asset.metadata, f"Asset {w_asset.id} missing author attribution"
                assert "commons_page_url" in w_asset.metadata, f"Asset {w_asset.id} missing commons_page_url"

    def test_latex_math_delimiters_balanced(self):
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                text = extract_all_text(block.content)
                issues = check_latex_balance(text)
                assert len(issues) == 0, (
                    f"LaTeX delimiter mismatch in block ID {block.id} (Page {block.page_number}): {issues}"
                )

    def test_zero_developer_leaks(self):
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                # Check title and page_title
                for title_field in [block.title, block.page_title]:
                    if title_field:
                        for pattern in DEVELOPER_LEAK_PATTERNS:
                            matches = re.findall(pattern, title_field, re.IGNORECASE)
                            assert len(matches) == 0, (
                                f"Developer term leak '{pattern}' in title '{title_field}' (Block {block.id})"
                            )

                # Check text content
                text = extract_all_text(block.content)
                for pattern in DEVELOPER_LEAK_PATTERNS:
                    matches = re.findall(pattern, text, re.IGNORECASE)
                    assert len(matches) == 0, (
                        f"Developer term leak '{pattern}' in block content (Block {block.id}, Page {block.page_number})"
                    )

    def test_worked_examples_multi_tier(self):
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            worked_examples = lesson.blocks.filter(block_type="worked_example")
            
            # Module 1.2 and 1.3 contain formal worked examples
            if "1.2" in unit.name:
                assert worked_examples.count() >= 5, f"Module 1.2 should contain 5 worked examples, found {worked_examples.count()}"
            elif "1.3" in unit.name:
                assert worked_examples.count() >= 1, f"Module 1.3 should contain at least 1 challenge worked example"

            for we in worked_examples:
                c = we.content
                assert "problem" in c, f"Worked example block {we.id} missing 'problem' key"
                assert "steps" in c, f"Worked example block {we.id} missing 'steps' key"
                assert len(c["steps"]) >= 3, f"Worked example block {we.id} must show multi-step reasoning"

    def test_knowledge_checks_validity(self):
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            kc_blocks = lesson.blocks.filter(block_type="knowledge_check")
            assert kc_blocks.count() >= 2, f"Lesson '{lesson.title}' must contain at least 2 knowledge check questions"
            
            for kc in kc_blocks:
                c = kc.content
                assert "question" in c, f"Knowledge check block {kc.id} missing 'question'"
                assert "answer" in c, f"Knowledge check block {kc.id} missing 'answer'"
                assert "explanation" in c, f"Knowledge check block {kc.id} missing 'explanation'"
                if c.get("check_type") == "multiple_choice":
                    assert "options" in c and len(c["options"]) >= 2, f"MCQ block {kc.id} must have options"

    def test_no_empty_placeholder_lesson_assets(self):
        topic = get_physics_topic()
        assert topic is not None
        
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            empty_assets = LessonAsset.objects.filter(
                lesson=lesson,
                file="",
                url__isnull=True,
                status="pending"
            )
            assert empty_assets.count() == 0, (
                f"Lesson '{lesson.title}' should NOT have empty pending placeholder LessonAssets in Stage 1"
            )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
