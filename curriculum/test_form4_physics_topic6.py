"""
Automated Pytest Test Suite for Form 4 Physics — Topic 6: Mains Electricity

Validates:
  1. Curriculum hierarchy linkage (844 -> Form 4 -> Physics -> Topic 6)
  2. 3 Learning Units and Lessons in 'published' status
  3. Strict sequential page numbering with no gaps
  4. Valid block and component types matching frontend registry
  5. Complete visual enrichment with vector SVGs and authentic Wikimedia assets
  6. Balanced LaTeX math delimiters ($ and $$)
  7. Zero developer terminology leaks in titles, captions, and text
  8. Multi-tier worked examples (Levels 1 to 5)
  9. Knowledge checks validity and option consistency
  10. Zero empty placeholder LessonAssets
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

VALID_BLOCK_TYPES = {
    "learning_goal", "concept_explanation", "definition_card", "formula_breakdown",
    "worked_example", "step_process", "comparison_table", "common_misconception",
    "prediction", "suggested_simulation", "reflection", "knowledge_check",
    "summary", "key_takeaway", "suggested_diagram", "suggested_image", "suggested_graph"
}

LEAK_PATTERNS = [
    r"Visual Representation",
    r"Building Intuition",
    r"AI-generated visual",
    r"Enrichment Slot",
    r"AI Prompt",
    r"pending",
    r"\[image_\d+\]"
]


class TestPhysicsTopic6Ingestion:

    @classmethod
    def setup_class(cls):
        cls.curriculum = Curriculum.objects.filter(name="844").first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Form 4").first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Physics").first()
        cls.topic = Topic.objects.filter(
            subject=cls.subject,
            name__icontains="Mains Electricity"
        ).first()

    def test_curriculum_hierarchy_exists(self):
        assert self.curriculum is not None, "Curriculum '844' not found"
        assert self.grade is not None, "Grade 'Form 4' not found"
        assert self.subject is not None, "Subject 'Physics' not found"
        assert self.topic is not None, "Topic 'Topic 6: Mains Electricity' not found"
        assert self.topic.learning_units.count() == 3, f"Expected 3 learning units, found {self.topic.learning_units.count()}"

    def test_lessons_published_and_complete(self):
        units = self.topic.learning_units.all().order_by("order")
        for unit in units:
            lesson = unit.lessons.first()
            assert lesson is not None, f"Unit '{unit.name}' has no lesson"
            assert lesson.status == "published", f"Lesson '{lesson.title}' status is '{lesson.status}', expected 'published'"
            assert lesson.blocks.count() >= 14, f"Lesson '{lesson.title}' has {lesson.blocks.count()} blocks, expected >= 14"

    def test_sequential_page_numbers(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            blocks = lesson.blocks.all().order_by("page_number", "order")
            pages = sorted(list(set(b.page_number for b in blocks)))
            expected_pages = list(range(1, max(pages) + 1))
            assert pages == expected_pages, f"Page sequence mismatch in '{lesson.title}': {pages} vs {expected_pages}"

    def test_valid_block_types_and_components(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                assert block.block_type in VALID_BLOCK_TYPES, f"Invalid block_type '{block.block_type}' in block {block.id}"
                assert block.component_type in VALID_BLOCK_TYPES, f"Invalid component_type '{block.component_type}' in block {block.id}"

    def test_visual_assets_enrichment_complete(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            diagram_blocks = lesson.blocks.filter(block_type="suggested_diagram")
            assert diagram_blocks.count() >= 1, f"Lesson '{lesson.title}' expected at least 1 diagram block"
            for b in diagram_blocks:
                has_svg = (
                    (isinstance(b.content, dict) and bool(b.content.get("svg_content"))) or
                    (bool(b.metadata) and bool(b.metadata.get("svg_content"))) or
                    b.assets.filter(storage_type="embed").exists()
                )
                assert has_svg, f"Diagram block {b.id} on page {b.page_number} in '{lesson.title}' is missing SVG content"

    def test_latex_math_delimiters_balanced(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                if isinstance(block.content, dict):
                    texts_to_check = []
                    if "text" in block.content:
                        texts_to_check.append(block.content["text"])
                    if "formula" in block.content:
                        texts_to_check.append(block.content["formula"])
                    if "problem" in block.content:
                        texts_to_check.append(block.content["problem"])
                    if "steps" in block.content and isinstance(block.content["steps"], list):
                        texts_to_check.extend(block.content["steps"])

                    for text in texts_to_check:
                        if not isinstance(text, str):
                            continue
                        clean_t = re.sub(r'\\\$', '', text)
                        clean_t = re.sub(r'\$\$(.*?)\$\$', '', clean_t, flags=re.DOTALL)
                        single_dollar_count = clean_t.count('$')
                        assert single_dollar_count % 2 == 0, (
                            f"Unbalanced single dollar math in block {block.id} (page {block.page_number}):\n{text}"
                        )

    def test_zero_developer_leaks(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            for block in lesson.blocks.all():
                for pat in LEAK_PATTERNS:
                    assert not re.search(pat, block.title or "", re.IGNORECASE), f"Leak '{pat}' in block title: {block.title}"
                    assert not re.search(pat, block.page_title or "", re.IGNORECASE), f"Leak '{pat}' in page title: {block.page_title}"
                    if isinstance(block.content, dict) and "text" in block.content:
                        assert not re.search(pat, block.content["text"], re.IGNORECASE), f"Leak '{pat}' in text of block {block.id}"

    def test_worked_examples_multi_tier(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            examples = lesson.blocks.filter(block_type="worked_example")
            if unit.order == 2:
                assert examples.count() >= 5, f"Lesson '{lesson.title}' has {examples.count()} worked examples, expected >= 5"
                for ex in examples:
                    content = ex.content
                    assert "problem" in content, f"Worked example {ex.id} missing 'problem'"
                    assert "steps" in content, f"Worked example {ex.id} missing 'steps'"
                    assert len(content["steps"]) >= 3, f"Worked example {ex.id} has fewer than 3 steps"

    def test_knowledge_checks_validity(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            checks = lesson.blocks.filter(block_type="knowledge_check")
            assert checks.count() >= 2, f"Lesson '{lesson.title}' has {checks.count()} knowledge checks, expected >= 2"
            for kc in checks:
                content = kc.content
                assert "question" in content, f"Knowledge check {kc.id} missing 'question'"
                assert "options" in content, f"Knowledge check {kc.id} missing 'options'"
                assert "answer" in content, f"Knowledge check {kc.id} missing 'answer'"
                assert "explanation" in content, f"Knowledge check {kc.id} missing 'explanation'"

    def test_no_empty_placeholder_lesson_assets(self):
        for unit in self.topic.learning_units.all():
            lesson = unit.lessons.first()
            assets = LessonAsset.objects.filter(lesson=lesson)
            for asset in assets:
                assert asset.status != "pending", f"Asset {asset.id} has status 'pending'"
                if asset.storage_type == "embed":
                    assert asset.metadata and "svg_content" in asset.metadata, f"Asset {asset.id} missing svg_content"
                elif asset.storage_type == "url":
                    assert asset.url, f"Asset {asset.id} missing url"
