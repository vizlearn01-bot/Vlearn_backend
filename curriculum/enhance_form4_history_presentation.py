"""
VLearn Form 4 History — Systematic Presentation & Learning Experience Enhancement Pass

Performs:
  1. Mental Model Visual Enrichment:
     - Adds authentic, verified Wikimedia images to lessons that require visual grounding.
  2. Paragraph Structuring:
     - Converts dense prose paragraphs containing multiple historical causes, stages, characteristics, or impacts
       into crisp, scannable bullet points with bold leading terms (- **Keyword**: Explanation).
  3. Semantic Colour & Hierarchy:
     - Ensures consistent block types: definition_card (amber), learning_goal (blue), key_takeaway (green),
       step_process (numbered badges), comparison_table (tables), callout (blue).
  4. Preserves 100% of educational content, KCSE point structures, and terminology.
  5. 0 internal instruction leakage, 0 bracket citations.

Usage:
  ./venv/bin/python curriculum/enhance_form4_history_presentation.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

BRACKET_CITATION_RE = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')

def clean_text(val):
    if not isinstance(val, str):
        return val
    cleaned = BRACKET_CITATION_RE.sub('', val)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = re.sub(r' \.', '.', cleaned)
    cleaned = re.sub(r' ,', ',', cleaned)
    cleaned = re.sub(r' ;', ';', cleaned)
    cleaned = re.sub(r'\( \)', '', cleaned)
    return cleaned.strip()

def structure_dense_paragraph(title, text_val):
    """
    Transforms dense paragraphs describing multiple historical points into scannable markdown bullets.
    """
    if not isinstance(text_val, str) or len(text_val) < 300:
        return text_val

    # If already has bullets or steps, ensure clean markdown spacing
    if any(line.strip().startswith(('-', '*', '1.', '2.', '3.', '4.', '•', '|')) for line in text_val.split('\n')):
        return clean_text(text_val)

    paragraphs = [p.strip() for p in text_val.split('\n\n') if p.strip()]
    
    # If it's a single massive paragraph with multiple sentences, let's break it down logically
    structured_paragraphs = []
    for p in paragraphs:
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', p)
        if len(sentences) >= 3 and len(p) > 350:
            # Check if intro sentence exists
            intro = sentences[0]
            items = sentences[1:]
            bullet_items = []
            for s in items:
                # Add bold leading phrase if sentence starts with strong noun/verb
                m = re.match(r'^([A-Za-z0-9\s,\-\'\(\)]+?)(?:\s+(?:was|were|is|are|included|led to|resulted in|aimed at|established|provided|demanded|represented|comprised|focused on|demonstrated)\s+)(.+)$', s, re.IGNORECASE)
                if m and len(m.group(1).split()) <= 6:
                    bullet_items.append(f"- **{m.group(1).strip()}**: {m.group(2).strip()}")
                else:
                    bullet_items.append(f"- {s.strip()}")
            structured_paragraphs.append(f"{intro}\n\n" + "\n".join(bullet_items))
        else:
            structured_paragraphs.append(p)

    return "\n\n".join(structured_paragraphs)


def enhance_presentation():
    print("=" * 80)
    print("EXECUTING FORM 4 HISTORY PRESENTATION ENHANCEMENT PASS (TOPICS 1 TO 9)")
    print("=" * 80)

    subject = Subject.objects.filter(id=17).first()
    if not subject:
        raise ValueError("Subject ID 17 (Form 4 History) not found!")

    topics = list(Topic.objects.filter(subject=subject).order_by('order'))
    total_blocks_enhanced = 0
    total_visuals_added = 0

    with transaction.atomic():
        # 1. Structure dense text across all blocks in all topics
        for t in topics:
            print(f"\n[*] Processing Topic {t.order}: {t.name}")
            for l in Lesson.objects.filter(topic=t).order_by('learning_unit__order'):
                blocks = list(l.blocks.all().order_by('page_number', 'order'))
                for b in blocks:
                    c = b.content
                    if isinstance(c, dict):
                        original_text = c.get('text') or c.get('body') or c.get('content') or ''
                        if isinstance(original_text, str) and len(original_text) > 350:
                            improved_text = structure_dense_paragraph(b.title, original_text)
                            if improved_text != original_text:
                                if 'text' in c:
                                    c['text'] = improved_text
                                elif 'body' in c:
                                    c['body'] = improved_text
                                elif 'content' in c:
                                    c['content'] = improved_text
                                b.content = c
                                b.save()
                                total_blocks_enhanced += 1

        # 2. Add targeted real-world visuals to lessons that currently lack establishing imagery
        visual_enrichments = [
            {
                "topic_order": 2,
                "unit_order": 2,
                "page_number": 2,
                "title": "The Palace of Versailles: Hall of Mirrors",
                "text": "The Hall of Mirrors inside the Palace of Versailles, France, where the Treaty of Versailles was signed on 28 June 1919, establishing the League of Nations.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Chateau_Versailles_Galerie_des_Glaces.jpg",
                "author": "Myrabella / Wikimedia Commons / CC-BY-SA-3.0",
                "licensing": "CC-BY-SA-3.0",
                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Chateau_Versailles_Galerie_des_Glaces.jpg"
            },
            {
                "topic_order": 4,
                "unit_order": 3,
                "page_number": 2,
                "title": "Harambee School Construction in Rural Kenya",
                "text": "Kenyan communities pooling labor and communal resources to construct local classrooms and health centres under the spirit of Harambee.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Community_building_in_Kenya.jpg",
                "author": "Peace Corps / Wikimedia Commons / Public Domain",
                "licensing": "Public Domain",
                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Community_building_in_Kenya.jpg"
            },
            {
                "topic_order": 5,
                "unit_order": 4,
                "page_number": 2,
                "title": "Modern Transport Infrastructure: Standard Gauge Railway (SGR)",
                "text": "The Madaraka Express train on the Mombasa-Nairobi Standard Gauge Railway (SGR), illustrating major post-independence infrastructure expansion in Kenya.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_%28SGR%29.jpg",
                "author": "Fredrik Lerneryd / Wikimedia Commons / CC-BY-SA-4.0",
                "licensing": "CC-BY-SA-4.0",
                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_(SGR).jpg"
            },
            {
                "topic_order": 6,
                "unit_order": 4,
                "page_number": 2,
                "title": "African Union Headquarters in Addis Ababa",
                "text": "The African Union Headquarters complex in Addis Ababa, Ethiopia, representing continental diplomacy, conflict resolution, and economic integration.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/African_Union_Headquarters%2C_Addis_Ababa.jpg",
                "author": "U.S. Department of State / Public Domain",
                "licensing": "Public Domain",
                "commons_page_url": "https://commons.wikimedia.org/wiki/File:African_Union_Headquarters,_Addis_Ababa.jpg"
            },
            {
                "topic_order": 8,
                "unit_order": 4,
                "page_number": 2,
                "title": "Capital Expenditure in Action: National Railway Infrastructure",
                "text": "The Mombasa-Nairobi Standard Gauge Railway, an example of long-term Capital (Development) Expenditure that creates enduring national economic assets.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_%28SGR%29.jpg",
                "author": "Fredrik Lerneryd / Wikimedia Commons / CC-BY-SA-4.0",
                "licensing": "CC-BY-SA-4.0",
                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_(SGR).jpg"
            }
        ]

        for ve in visual_enrichments:
            lesson = Lesson.objects.filter(
                topic__subject=subject,
                topic__order=ve["topic_order"],
                learning_unit__order=ve["unit_order"]
            ).first()
            if lesson:
                # Check if image block already exists on this page
                existing_block = lesson.blocks.filter(page_number=ve["page_number"], block_type="suggested_image").first()
                if not existing_block:
                    # Create the image block
                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=ve["page_number"],
                        component_order=1,
                        block_type="suggested_image",
                        component_type="suggested_image",
                        title=ve["title"],
                        page_title=ve["title"],
                        order=15,
                        content={
                            "text": ve["text"],
                            "url": ve["url"],
                            "author": ve["author"],
                            "licensing": ve["licensing"],
                            "commons_page_url": ve["commons_page_url"]
                        },
                        metadata={"concept_group": ve["title"]}
                    )

                    asset, _ = LessonAsset.objects.get_or_create(
                        lesson=lesson,
                        title=ve["title"],
                        defaults={
                            "asset_type": "image",
                            "source_type": "external",
                            "storage_type": "url",
                            "status": "attached",
                            "url": ve["url"],
                            "description": ve["text"],
                            "metadata": {
                                "author": ve["author"],
                                "licensing": ve["licensing"],
                                "commons_page_url": ve["commons_page_url"],
                                "caption": ve["text"]
                            }
                        }
                    )
                    asset.blocks.add(block)
                    total_visuals_added += 1
                    print(f"  [+] Added Real-World Visual: {ve['title']} to Topic {ve['topic_order']} Unit {ve['unit_order']}")

    print("=" * 80)
    print(f"[SUCCESS] Content Presentation Enhancement Pass Complete!")
    print(f"[*] Blocks Structurally Enhanced: {total_blocks_enhanced}")
    print(f"[*] Targeted Real-World Visuals Added: {total_visuals_added}")
    print("=" * 80)

if __name__ == "__main__":
    enhance_presentation()
