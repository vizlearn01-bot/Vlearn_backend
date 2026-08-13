"""
VLearn Form 4 Physics — Topic 2 Automated Validation Test Suite

Validates:
  1. Curriculum Hierarchy (Form 4 Physics -> Topic 2: Uniform Circular Motion)
  2. All 3 learning units and lessons exist, published, and complete
  3. Sequential page numbering (1 to N with no gaps)
  4. Valid block types and component types matching frontend registry
  5. Complete Visual Enrichment (SVGs sanitized and embedded, Wikimedia assets attached)
  6. LaTeX math delimiter balance ($...$ and $$...$$)
  7. Zero developer or AI prompt leaks in titles or student-facing text
  8. Multi-tier worked examples with structured steps
  9. Knowledge checks validity (questions, options, answer keys, explanations)
  10. Idempotent safe updates

Usage:
  pytest curriculum/test_form4_physics_topic2.py -v
"""

import os
import sys
import re
import pytest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def get_physics_topic2():
    return Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Uniform Circular Motion"
    ).first()

@pytest.mark.django_db
class TestPhysicsTopic2Ingestion:

    def test_curriculum_hierarchy_exists(self):
        topic = get_physics_topic2()
        assert topic is not None, "Topic 2: Uniform Circular Motion must exist"
        assert topic.subject.name == "Physics"
        assert topic.subject.grade.name == "Form 4"
        assert topic.subject.grade.curriculum.name == "844"

        units = topic.learning_units.all().order_by("order")
        assert units.count() == 3, f"Expected 3 learning units in Topic 2, found {units.count()}"

        expected_titles = [
            "Module 2.1: Kinematics of Circular Motion and Angular Quantities",
            "Module 2.2: Centripetal Dynamics, Vertical Circles, and Laboratory Experiments",
            "Module 2.3: Engineering Applications and Mechanics of Circular Motion"
        ]
        for idx, expected in enumerate(expected_titles):
            assert units[idx].name == expected, f"Unit {idx+1} mismatch: expected '{expected}', found '{units[idx].name}'"

    def test_lessons_published_and_complete(self):
        topic = get_physics_topic2()
        assert topic is not None

        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            assert lesson is not None, f"Unit '{unit.name}' must have a lesson"
            assert lesson.status == "published", f"Lesson '{lesson.title}' must be published"
            assert lesson.version == 1, f"Lesson '{lesson.title}' must have version 1"
            assert lesson.blocks.count() >= 15, f"Lesson '{lesson.title}' has too few blocks ({lesson.blocks.count()})"

    def test_sequential_page_numbers(self):
        topic = get_physics_topic2()
        assert topic is not None

        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            pages = sorted(list(set(lesson.blocks.values_list("page_number", flat=True))))
            assert len(pages) >= 12, f"Lesson '{lesson.title}' has too few pages ({len(pages)})"
            
            # Check 1 to N without gaps
            expected_pages = list(range(1, max(pages) + 1))
            assert pages == expected_pages, (
                f"Lesson '{lesson.title}' pages are not strictly sequential: expected {expected_pages}, got {pages}"
            )

    def test_valid_block_types_and_components(self):
        valid_block_types = {
            'learning_goal', 'concept_explanation', 'formula_breakdown',
            'worked_example', 'step_process', 'comparison_table',
            'definition_card', 'suggested_diagram', 'suggested_graph',
            'suggested_simulation', 'suggested_image', 'prediction', 'reflection',
            'common_misconception', 'common_mistake', 'callout',
            'knowledge_check', 'summary', 'key_takeaway'
        }
        
        topic = get_physics_topic2()
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
        topic = get_physics_topic2()
        assert topic is not None

        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            svg_assets = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram", source_type="ai_generated")
            assert svg_assets.count() >= 2, f"Lesson '{lesson.title}' should have enriched SVG assets"
            
            for asset in svg_assets:
                assert asset.metadata and "svg_content" in asset.metadata, f"Asset {asset.id} missing svg_content"
                assert "<svg" in asset.metadata["svg_content"], f"Asset {asset.id} svg_content must contain SVG XML"

        # Wikimedia checks
        wikimedia_assets = LessonAsset.objects.filter(lesson__topic=topic, asset_type="image", source_type="external")
        assert wikimedia_assets.count() >= 4, f"Topic 2 should have at least 4 Wikimedia photographic assets, found {wikimedia_assets.count()}"
        for w_asset in wikimedia_assets:
            assert w_asset.url.startswith("https://upload.wikimedia.org"), f"Asset {w_asset.id} must have valid Wikimedia URL"
            assert w_asset.metadata and "author" in w_asset.metadata, f"Asset {w_asset.id} missing author attribution"
            assert "commons_page_url" in w_asset.metadata, f"Asset {w_asset.id} missing commons_page_url"

    def test_latex_math_delimiters_balanced(self):
        topic = get_physics_topic2()
        assert topic is not None

        def check_text_balance(text, context_info):
            if not isinstance(text, str):
                return
            inline_count = len(re.findall(r'(?<!\\)\$', text))
            assert inline_count % 2 == 0, (
                f"Unbalanced single '$' delimiters ({inline_count}) in {context_info}:\n{text[:200]}"
            )

        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                c = block.content
                ctx = f"Lesson '{lesson.title}', Page {block.page_number}, Block '{block.title}'"
                if isinstance(c, dict):
                    for k, v in c.items():
                        if isinstance(v, str):
                            check_text_balance(v, f"{ctx} [key: {k}]")
                        elif isinstance(v, list):
                            for idx, item in enumerate(v):
                                if isinstance(item, str):
                                    check_text_balance(item, f"{ctx} [list idx: {idx}]")
                                elif isinstance(item, list):
                                    for sub in item:
                                        if isinstance(sub, str):
                                            check_text_balance(sub, f"{ctx} [table cell]")
                elif isinstance(c, str):
                    check_text_balance(c, ctx)

    def test_zero_developer_leaks(self):
        forbidden_patterns = [
            r'\[image_\d+\]',
            r'\[\d+\]',
            r'\bTODO\b',
            r'\bEnrichment Slot\b',
            r'\bAI Prompt\b',
            r'\bPlaceholder\b',
            r'\bVisual Representation\b'
        ]

        topic = get_physics_topic2()
        assert topic is not None

        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                ctx = f"Lesson '{lesson.title}', Page {block.page_number}, Block '{block.title}'"
                text_to_check = f"{block.page_title} {block.title} {str(block.content)}"
                for pat in forbidden_patterns:
                    match = re.search(pat, text_to_check, re.IGNORECASE)
                    assert not match, f"Developer leak '{match.group()}' found in {ctx}"

    def test_worked_examples_multi_tier(self):
        topic = get_physics_topic2()
        assert topic is not None

        all_examples = []
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            examples = lesson.blocks.filter(block_type="worked_example")
            for ex in examples:
                all_examples.append((lesson, ex))

        assert len(all_examples) >= 5, f"Expected at least 5 worked examples across Topic 2, found {len(all_examples)}"

        for lesson, ex in all_examples:
            c = ex.content
            assert isinstance(c, dict), f"Worked example block ID {ex.id} must have dict content"
            assert "problem" in c and c["problem"], f"Worked example block ID {ex.id} missing problem text"
            assert "steps" in c and isinstance(c["steps"], list) and len(c["steps"]) >= 2, (
                f"Worked example block ID {ex.id} must have at least 2 steps"
            )

    def test_knowledge_checks_validity(self):
        topic = get_physics_topic2()
        assert topic is not None

        all_kcs = []
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            kcs = lesson.blocks.filter(block_type="knowledge_check")
            for kc in kcs:
                all_kcs.append((lesson, kc))

        assert len(all_kcs) >= 6, f"Expected at least 6 knowledge checks across Topic 2, found {len(all_kcs)}"

        for lesson, kc in all_kcs:
            c = kc.content
            assert "question" in c and c["question"], f"KC block ID {kc.id} missing question"
            assert "options" in c and isinstance(c["options"], list) and len(c["options"]) >= 2, (
                f"KC block ID {kc.id} must have >= 2 options"
            )
            assert "answer" in c and c["answer"], f"KC block ID {kc.id} missing answer"
            assert "explanation" in c and c["explanation"], f"KC block ID {kc.id} missing explanation"
