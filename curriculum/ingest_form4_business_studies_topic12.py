"""
VLearn Form 4 Business Studies — Topic 12 Ingestion Engine (A Trial Balance)
Authoritative Django Ingestion Script.
"""

import sys
import os
import argparse
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from django.utils import timezone
from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.topic12_data import TOPIC12_UNITS


def clean_bracket_citations(text):
    """Strip bracketed citations from text."""
    if not isinstance(text, str):
        return text
    import re
    cleaned = re.sub(r'\s*\[\d+(?:,\s*\d+)*\]', '', text)
    return cleaned.strip()


def sanitize_content_dict(content_dict):
    """Recursively clean bracket citations in content dictionary strings."""
    if isinstance(content_dict, str):
        return clean_bracket_citations(content_dict)
    elif isinstance(content_dict, dict):
        return {k: sanitize_content_dict(v) for k, v in content_dict.items()}
    elif isinstance(content_dict, list):
        return [sanitize_content_dict(item) for item in content_dict]
    return content_dict


def normalize_block_type(component_type):
    """Map frontend component types to backend block types."""
    mapping = {
        "learning_goal": "text",
        "concept_card": "text",
        "definition_card": "text",
        "summary": "text",
        "worked_example": "worked_example",
        "comparison_table": "table",
        "photo_view": "suggested_image",
        "svg_viewer": "suggested_diagram",
        "knowledge_check": "mcq_interactive"
    }
    return mapping.get(component_type, "text")


@transaction.atomic
def ingest_topic12(replace=False):
    print("=" * 80)
    print("STARTING FORM 4 BUSINESS STUDIES TOPIC 12 INGESTION ENGINE (A TRIAL BALANCE)")
    print("=" * 80)

    # 1. Resolve Hierarchy
    curriculum, _ = Curriculum.objects.get_or_create(
        name="844",
        defaults={"description": "Kenyan 8-4-4 System of Education"}
    )
    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Form 4",
        defaults={"level": 4, "description": "Form 4 National Curriculum"}
    )
    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Business Studies",
        defaults={"description": "Form 4 Business Studies"}
    )

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Grade: {grade.name} (ID: {grade.id})")
    print(f"[*] Subject: {subject.name} (ID: {subject.id})")

    # 2. Topic 12: A Trial Balance
    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=12,
        defaults={
            "name": "A Trial Balance",
            "description": "Definition, purpose, and standard format of a Trial Balance, DR. EXP (Drawings, Assets, Expenses) vs CR. LIC (Capital, Revenues, Liabilities) placement rules, extracting trial balances (San Enterprises, Kiboko Traders, Dipa Traders), errors disclosed by a trial balance (totals mismatch), 6 errors not disclosed by a trial balance (omission, commission, principle, compensation, complete reversal, original entry), reconstructing incorrect trial balances (Onyati case study), and KCSE essay mastery."
        }
    )
    if topic.name != "A Trial Balance":
        topic.name = "A Trial Balance"
        topic.description = "Definition, purpose, and standard format of a Trial Balance, DR. EXP (Drawings, Assets, Expenses) vs CR. LIC (Capital, Revenues, Liabilities) placement rules, extracting trial balances (San Enterprises, Kiboko Traders, Dipa Traders), errors disclosed by a trial balance (totals mismatch), 6 errors not disclosed by a trial balance (omission, commission, principle, compensation, complete reversal, original entry), reconstructing incorrect trial balances (Onyati case study), and KCSE essay mastery."
        topic.save()

    print(f"[*] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    if replace:
        print("[!] --replace flag supplied: Cleaning existing units and lessons for Topic 12...")
        LearningUnit.objects.filter(topic=topic).delete()

    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    now = timezone.now()

    # 3. Ingest Learning Units & Lessons
    for unit_idx, unit_data in enumerate(TOPIC12_UNITS, start=1):
        unit_name = clean_bracket_citations(unit_data["unit_name"])
        lesson_title = clean_bracket_citations(unit_data["lesson_title"])

        learning_unit = LearningUnit.objects.create(
            topic=topic,
            name=unit_name,
            description=f"Form 4 Business Studies Topic 12 Unit {unit_idx}: {unit_name}",
            order=unit_idx
        )

        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=learning_unit,
            title=lesson_title,
            status="published",
            version=1,
            published_at=now
        )
        total_lessons += 1

        print(f"\n  [+] Ingesting Unit {unit_idx}: '{unit_name}' -> Lesson: '{lesson_title}'")

        block_global_order = 1

        for page in unit_data["pages"]:
            page_num = page["page_number"]
            page_title = clean_bracket_citations(page["page_title"])
            total_pages += 1

            for block_num, b_data in enumerate(page["blocks"], start=1):
                comp_type = b_data.get("component_type", "concept_card")
                backend_type = normalize_block_type(comp_type)
                title = clean_bracket_citations(b_data.get("title", page_title))

                raw_content = b_data.get("content", {})
                sanitized_content = sanitize_content_dict(raw_content)

                # Construct block
                block_kwargs = {
                    "lesson": lesson,
                    "block_id": f"L12U{unit_idx}P{page_num}B{block_num}",
                    "block_type": backend_type,
                    "title": title,
                    "content": sanitized_content if isinstance(sanitized_content, dict) else {"text": str(sanitized_content)},
                    "order": block_global_order,
                    "page_number": page_num,
                    "page_title": page_title,
                    "component_type": comp_type,
                    "component_order": block_num,
                    "metadata": {
                        "topic": "A Trial Balance",
                        "unit_order": unit_idx,
                        "page_number": page_num
                    }
                }

                # Handle SVG Markup
                if comp_type == "svg_viewer" and "svg_content" in b_data:
                    block_kwargs["content"]["svg_markup"] = b_data["svg_content"]
                    block_kwargs["content"]["svg_content"] = b_data["svg_content"]

                block = LessonBlock.objects.create(**block_kwargs)
                total_blocks += 1
                block_global_order += 1

                # Asset handling
                if comp_type == "photo_view" and isinstance(sanitized_content, dict) and "url" in sanitized_content:
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="image",
                        source_type="external",
                        storage_type="url",
                        status="ready",
                        title=title,
                        description=sanitized_content.get("text", title),
                        url=sanitized_content["url"],
                        metadata={
                            "author": sanitized_content.get("author", "Wikimedia"),
                            "licensing": sanitized_content.get("licensing", "CC BY-SA 4.0"),
                            "commons_page_url": sanitized_content.get("commons_page_url", "")
                        }
                    )
                    asset.blocks.add(block)
                    total_assets += 1

                elif comp_type == "svg_viewer" and "svg_content" in b_data:
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        source_type="generated",
                        storage_type="inline_svg",
                        status="ready",
                        title=title,
                        description=sanitized_content.get("text", title),
                        metadata={"vector_format": "SVG"}
                    )
                    asset.blocks.add(block)
                    total_assets += 1

        print(f"      [OK] Ingested {len(unit_data['pages'])} Pages for Lesson {unit_idx}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Business Studies Topic 12 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print(f"[*] Total Media Assets:     {total_assets}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 Business Studies Topic 12")
    parser.add_argument("--replace", action="store_true", help="Replace existing Topic 12 content")
    args = parser.parse_args()

    ingest_topic12(replace=args.replace)
