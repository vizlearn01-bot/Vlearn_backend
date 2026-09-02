"""
VLearn CBC Grade 10 ICT — Topic 4: Word Processing
Production Ingestion & Pedagogical Enrichment Engine

Target:
- Curriculum: CBC
- Grade: Grade 10 (Level: 10)
- Subject: ICT
- Topic: Word Processing (Order: 4)

Decomposed into 10 Learning Units & 10 Published 5-Page Lessons:
  1. Lesson 4.1.1: Meaning and Importance of Word Processing
  2. Lesson 4.1.2: Selection of Word Processing Applications
  3. Lesson 4.1.3: Fundamental Word Processing Tasks
  4. Lesson 4.1.4: Character and Paragraph Formatting
  5. Lesson 4.1.5: Page Layout and Formatting
  6. Lesson 4.1.6: Automated Proofreading and Editing Tools
  7. Lesson 4.1.7: Inserting and Formatting Tables
  8. Lesson 4.1.8: Section Breaks, Styles, and Page Formatting
  9. Lesson 4.1.9: Graphics, Table of Figures, Hyperlinks, and Cross-Referencing
  10. Lesson 4.1.10: Collaborating with Peers, Mail Merge, and Sharing
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.cbc_grade10_ict_topic4_data import TOPIC_4_LESSONS

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes markdown typography."""
    if not text:
        return ""
    # Strip bracket citations e.g. [36], [258, 262]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Normalize bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def ingest_grade10_ict_topic4(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 4: Word Processing (Grade 10 ICT)")
    print("=" * 80)

    # 1. Resolve Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' not found in database!")

    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC!")

    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="ICT",
        defaults={"description": "Senior Secondary ICT Curriculum (Grade 10 CBC)"}
    )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=4,
        defaults={
            "name": "Word Processing",
            "description": "Word processing software fundamentals, application selection, typing ergonomics, typography, page layouts, automated proofreading, tables, styles, graphics, mail merge, and peer collaboration."
        }
    )
    if not t_created:
        topic.name = "Word Processing"
        topic.description = "Word processing software fundamentals, application selection, typing ergonomics, typography, page layouts, automated proofreading, tables, styles, graphics, mail merge, and peer collaboration."
        topic.save()
    print(f"[*] Resolved Topic 4: {topic.name} (ID: {topic.id})")

    # 2. Clear Existing Data for Topic 4 if Replace is True
    if replace:
        print("[*] Replacing existing Topic 4 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    # 3. Ingest Units and Lessons inside Atomic Transaction
    with transaction.atomic():
        for item in TOPIC_4_LESSONS:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Senior ICT Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "ICT",
                    "topic_order": 4,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_ict_t4_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 4, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAsset if applicable
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA 4.0"),
                                "caption": b_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("description", b_title),
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print(f"TOPIC 4 (WORD PROCESSING) INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_ict_topic4(replace=True)
