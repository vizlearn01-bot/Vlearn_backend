"""
VLearn Form 4 Physics — Topic 1 Audit Tool
Displays curriculum hierarchy, learning units, lessons, page distributions,
block types, formula breakdowns, worked examples, and visual opportunity slots.

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/audit_form4_physics.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def audit_physics():
    print("=" * 100)
    print("VLEARN FORM 4 PHYSICS — CURRICULUM AUDIT REPORT")
    print("=" * 100)

    subject = Subject.objects.filter(
        grade__name="Form 4",
        name="Physics"
    ).first()

    if not subject:
        print("ERROR: Subject 'Physics' not found under Form 4!")
        return

    print(f"Subject: {subject.name} (ID: {subject.id}) | Grade: {subject.grade.name} | Curriculum: {subject.grade.curriculum.name}")
    print(f"Topics Count: {subject.topics.count()}\n")

    for topic in subject.topics.all().order_by("order"):
        print(f"--- TOPIC {topic.order}: {topic.name} (ID: {topic.id}) ---")
        units = topic.learning_units.all().order_by("order")
        print(f"Learning Units: {units.count()}")

        for unit in units:
            lesson = unit.lessons.first()
            if not lesson:
                print(f"  [Unit {unit.order}] {unit.name} --> NO LESSON FOUND!")
                continue

            blocks = lesson.blocks.all().order_by("order")
            pages = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            block_types = [b.block_type for b in blocks]
            visual_slots = [b for b in blocks if b.block_type in ['suggested_diagram', 'suggested_graph', 'suggested_table', 'suggested_simulation']]
            worked_examples = [b for b in blocks if b.block_type == 'worked_example']
            knowledge_checks = [b for b in blocks if b.block_type == 'knowledge_check']
            formula_blocks = [b for b in blocks if b.block_type == 'formula_breakdown']

            print(f"  [Unit {unit.order}] {unit.name}")
            print(f"    Lesson ID: {lesson.id} | Title: '{lesson.title}' | Status: {lesson.status}")
            print(f"    Pages ({len(pages)}): {pages[0]} to {pages[-1]} | Total Blocks: {blocks.count()}")
            print(f"    Formula Breakdowns: {len(formula_blocks)} | Worked Examples: {len(worked_examples)}")
            print(f"    Knowledge Checks: {len(knowledge_checks)} | Visual Opportunity Slots: {len(visual_slots)}")
            
            for v_block in visual_slots:
                print(f"      - [Page {v_block.page_number}] {v_block.block_type}: '{v_block.title}'")
            print()

    print("=" * 100)

if __name__ == "__main__":
    audit_physics()
