"""
VLearn CBC Grade 10 CRE — Sub-Strand 2.2: Infancy and Early Life of Jesus Christ
Production Database Ingestion Engine
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.cbc_grade10_cre_topic2_2_data import TOPIC_2_2_DATA, TOPIC_2_2_LESSONS


def clean_text(text: str) -> str:
    """Removes bracket citations and internal tags, normalizes whitespace."""
    if not text:
        return ""
    # Strip bracket citations e.g. [53], [121, 207], [208]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal prompt / visual tags
    text = re.sub(r'\[(?:VISUAL|BIBLE PASSAGE|CRITICAL THINKING|REAL WORLD APPLICATION):?[^\]]*\]', '', text)
    # Normalize markdown bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()


def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        # Do not clean SVG code with text sanitizer to preserve SVG syntax
        if data.strip().startswith("<svg"):
            return data.strip()
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


def ingest_grade10_cre_topic2_2(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 2.2: Infancy and Early Life of Jesus Christ (Grade 10 CRE)")
    print("=" * 80)

    # 1. Resolve Curriculum & Grade
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        raise RuntimeError("Curriculum 'CBC' (ID 5) not found!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        raise RuntimeError("Grade 10 not found under CBC!")

    # 2. Resolve Subject (CRE, ID 46)
    subject = Subject.objects.filter(id=46).first() or Subject.objects.filter(grade=grade, name__icontains="CRE").first()
    if not subject:
        subject = Subject.objects.create(
            id=46,
            grade=grade,
            name="CRE",
            description="Christian Religious Education Curriculum (Grade 10 CBC)"
        )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    # 3. Resolve / Create Topic (Order 12)
    topic_order = TOPIC_2_2_DATA["topic_order"]
    topic_name = TOPIC_2_2_DATA["topic_name"]
    topic_desc = TOPIC_2_2_DATA["topic_description"]

    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=topic_order,
        defaults={
            "name": topic_name,
            "description": topic_desc
        }
    )
    if not t_created:
        topic.name = topic_name
        topic.description = topic_desc
        topic.save()
    print(f"[*] Resolved Topic: {topic.name} (Order: {topic.order}, ID: {topic.id})")

    # 4. Clean existing if replace=True
    if replace:
        print("[*] Replacing existing Topic 2.2 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for item in TOPIC_2_2_LESSONS:
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
                    "author": "VLearn Grade 10 CRE Curriculum Ingestion Agent",
                    "grade": "Grade 10",
                    "subject": "CRE",
                    "topic_order": topic_order,
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
                        block_id=f"g10_cre_t2_2_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": topic_order, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAsset if applicable
                    if b_type == "suggested_image" and "url" in b_content:
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

                    elif b_type == "suggested_diagram" and "svg" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg"]}
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
    print("TOPIC 2.2 INGESTION COMPLETE:")
    print(f"  Topic ID:        {topic.id} (Order: {topic.order})")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)
    return {
        "topic_id": topic.id,
        "units": total_units,
        "lessons": total_lessons,
        "pages": total_pages,
        "blocks": total_blocks,
        "assets": total_assets
    }


if __name__ == "__main__":
    ingest_grade10_cre_topic2_2(replace=True)
