"""
VLearn Form 4 Business Studies — Topic 2: Population and Employment
Authoritative Ingestion Engine

Subject: Business Studies (Subject ID: 23)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)
Topic 2: Population and Employment (Order: 2)

Architecture:
  6 Learning Units / Lessons:
  - Lesson 1: Population Growth and Demographic Concepts (10 Pages)
  - Lesson 2: Optimum, Under-population, and Over-population (10 Pages)
  - Lesson 3: Population Structure, Age Distribution, and Dependency (10 Pages)
  - Lesson 4: Population Dynamics in National Development (9 Pages)
  - Lesson 5: Employment and Types & Causes of Unemployment (11 Pages)
  - Lesson 6: Solutions to Unemployment & KCSE Mastery (10 Pages)
  Total: 60 Pages

Features:
  - 100% pedagogical fidelity to Lessons.md and form4_business_studies_extraction.md
  - Automated regex cleaning of all bracket citations ([145], [146], [249], [250])
  - 6-step progressive dependency ratio and per-capita GDP calculations
  - Custom dark-mode SVG vector diagrams and authentic verified Wikimedia assets
  - Idempotent and transactional database execution

Usage:
  ./venv/bin/python curriculum/ingest_form4_business_studies_topic2.py [--replace]
"""

import os
import sys
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

from curriculum.topic2_data import (
    LESSON_1_DATA, LESSON_2_DATA, LESSON_3_DATA,
    LESSON_4_DATA, LESSON_5_DATA, LESSON_6_DATA
)

ALL_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA,
    LESSON_6_DATA
]

def clean_text(raw_str):
    """Remove source citation brackets like [145], [146], [249] and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data

def run_ingestion(replace=False):
    print("=" * 80)
    print("STARTING FORM 4 BUSINESS STUDIES TOPIC 2 INGESTION ENGINE (POPULATION AND EMPLOYMENT)")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Hierarchy
        curriculum, _ = Curriculum.objects.get_or_create(
            name="844",
            defaults={"description": "Kenyan 8-4-4 National Curriculum"}
        )
        print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")

        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Form 4",
            defaults={"level": 4, "description": "Form 4 Secondary"}
        )
        print(f"[*] Grade: {grade.name} (ID: {grade.id})")

        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Business Studies",
            defaults={"description": "Secondary Business Studies Form 4"}
        )
        print(f"[*] Subject: {subject.name} (ID: {subject.id})")

        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            name="Population and Employment",
            defaults={
                "order": 2,
                "description": (
                    "Covers demographic concepts, optimum/under/over population, population structure, "
                    "dependency ratio, implications on national development, concepts of employment, "
                    "types and causes of unemployment, and policy solutions to unemployment in Kenya."
                )
            }
        )
        topic.order = 2
        topic.save()
        print(f"[*] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

        if replace:
            print("[!] --replace flag supplied: Cleaning existing units and lessons for Topic 2...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()

        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # Ingest Lessons
        for lesson_data in ALL_LESSONS:
            unit_order = lesson_data["unit_order"]
            unit_name = lesson_data["unit_name"]
            lesson_title = lesson_data["lesson_title"]
            pages = lesson_data["pages"]

            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": f"Learning Unit {unit_order}: {unit_name}"}
            )
            unit.name = unit_name
            unit.save()

            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": lesson_title,
                    "status": "published",
                    "version": 1
                }
            )
            lesson.title = lesson_title
            lesson.status = "published"
            lesson.save()

            print(f"  [+] Ingesting Unit {unit_order}: '{unit_name}' -> Lesson: '{lesson_title}'")

            block_order_counter = 10

            for page in pages:
                page_num = page["page_number"]
                page_title = page["page_title"]
                blocks = page["blocks"]
                total_pages += 1

                for comp_idx, block_info in enumerate(blocks, 1):
                    b_type = block_info["block_type"]
                    c_type = block_info["component_type"]

                    if b_type == "text":
                        if c_type == "learning_goal": b_type = "learning_goal"
                        elif c_type == "definition_card": b_type = "definition_card"
                        elif c_type == "concept_card": b_type = "concept_explanation"
                        elif c_type == "summary_card": b_type = "summary"
                        elif c_type == "step_process": b_type = "step_process"
                        elif c_type == "table_view": b_type = "comparison_table"
                        elif c_type == "photo_view": b_type = "suggested_image"
                        elif c_type == "svg_viewer": b_type = "suggested_diagram"
                        elif c_type == "mcq_interactive": b_type = "knowledge_check"
                        else: b_type = "concept_explanation"

                    b_title = block_info.get("title", page_title)
                    b_content = clean_content_dict(block_info.get("content", {}))

                    # Process SVG if specified in block
                    svg_markup = block_info.get("svg_content")

                    metadata = {"concept_group": page_title}
                    if svg_markup:
                        metadata["svg_content"] = svg_markup
                        if isinstance(b_content, dict):
                            b_content["svg_content"] = svg_markup
                            b_content["svg"] = svg_markup

                    block, b_created = LessonBlock.objects.get_or_create(
                        lesson=lesson,
                        page_number=page_num,
                        component_order=comp_idx,
                        defaults={
                            "block_type": b_type,
                            "component_type": c_type,
                            "title": b_title,
                            "page_title": page_title,
                            "order": block_order_counter,
                            "content": b_content,
                            "metadata": metadata
                        }
                    )

                    if not b_created:
                        block.block_type = b_type
                        block.component_type = c_type
                        block.title = b_title
                        block.page_title = page_title
                        block.order = block_order_counter
                        block.content = b_content
                        block.metadata = metadata
                        block.save()

                    # Handle Media & Diagram Assets
                    if b_type == "suggested_image" and isinstance(b_content, dict) and b_content.get("url"):
                        media_url = b_content.get("url")
                        author = b_content.get("author", "Educational Resource")
                        licensing = b_content.get("licensing", "Standard")
                        commons_page_url = b_content.get("commons_page_url", "")

                        asset, a_created = LessonAsset.objects.get_or_create(
                            lesson=lesson,
                            title=b_title,
                            defaults={
                                "asset_type": "image",
                                "source_type": "external",
                                "storage_type": "url",
                                "status": "attached",
                                "url": media_url,
                                "description": b_content.get("text", b_title),
                                "metadata": {
                                    "author": author,
                                    "licensing": licensing,
                                    "commons_page_url": commons_page_url,
                                    "caption": b_content.get("text", b_title)
                                }
                            }
                        )
                        if not a_created:
                            asset.url = media_url
                            asset.status = "attached"
                            asset.asset_type = "image"
                            asset.metadata = {
                                "author": author,
                                "licensing": licensing,
                                "commons_page_url": commons_page_url,
                                "caption": b_content.get("text", b_title)
                            }
                            asset.save()

                        asset.blocks.add(block)
                        total_assets += 1

                    elif (b_type == "suggested_diagram" or svg_markup):
                        asset, a_created = LessonAsset.objects.get_or_create(
                            lesson=lesson,
                            title=b_title,
                            defaults={
                                "asset_type": "diagram",
                                "source_type": "ai_generated",
                                "storage_type": "embed",
                                "status": "attached",
                                "description": b_content.get("text", b_title) if isinstance(b_content, dict) else b_title,
                                "metadata": {
                                    "svg_content": svg_markup or "",
                                    "caption": b_title
                                }
                            }
                        )
                        if not a_created:
                            asset.status = "attached"
                            asset.asset_type = "diagram"
                            asset.metadata = {
                                "svg_content": svg_markup or "",
                                "caption": b_title
                            }
                            asset.save()

                        asset.blocks.add(block)
                        total_assets += 1

                    block_order_counter += 10
                    total_blocks += 1

            print(f"      [OK] Ingested {len(pages)} Pages for Lesson {unit_order}.")

        print("=" * 80)
        print("[SUCCESS] Form 4 Business Studies Topic 2 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 Business Studies Topic 2")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
