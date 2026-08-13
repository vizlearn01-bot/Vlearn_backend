"""
VLearn Form 4 Geography — Comprehensive Inspection & Quality Audit

Generates a detailed diagnostic audit of all ingested Form 4 Geography Topics:
- Topic 1: Land Reclamation and Rehabilitation
- Topic 2: Fishing

Reports per-lesson block distributions, page counts, visual attachments, and humanization integrity.

Usage:
  ./venv/bin/python curriculum/audit_form4_geography.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def audit_form4_geography():
    print("=" * 80)
    print("VLEARN FORM 4 GEOGRAPHY: COMPREHENSIVE CURRICULUM AUDIT")
    print("=" * 80)

    topics = list(Topic.objects.filter(subject__name="Geography", subject__grade__name="Form 4").order_by("order"))
    if not topics:
        print("[!] No Form 4 Geography Topics found!")
        return

    grand_pages = 0
    grand_blocks = 0
    grand_svgs = 0
    grand_photos = 0
    grand_checks = 0
    grand_assets = 0

    for topic in topics:
        print(f"\n" + "=" * 80)
        print(f"TOPIC {topic.order}: {topic.name} (ID: {topic.id})")
        print("=" * 80)

        lessons = list(topic.lessons.all().order_by("learning_unit__order"))
        t_pages = 0
        t_blocks = 0
        t_svgs = 0
        t_photos = 0
        t_checks = 0

        for idx, lesson in enumerate(lessons, 1):
            u = lesson.learning_unit
            blocks = list(lesson.blocks.all().order_by("order"))
            pages = {}
            for b in blocks:
                p_num = b.page_number or 1
                if p_num not in pages:
                    pages[p_num] = []
                pages[p_num].append(b)

            t_pages += len(pages)
            t_blocks += len(blocks)

            print(f"\n" + "-" * 70)
            print(f"LESSON {idx}: {lesson.title} (ID: {lesson.id})")
            print(f"Learning Unit: {u.name} (Order: {u.order}) | Status: {lesson.status} | Version: {lesson.version}")
            print(f"Total Pages: {len(pages)} | Total Blocks: {len(blocks)} | Assets Attached: {lesson.assets.count()}")
            print("-" * 70)

            for p_num in sorted(pages.keys()):
                p_blocks = pages[p_num]
                p_title = p_blocks[0].page_title if p_blocks else "Untitled Page"
                comp_types = [b.block_type for b in p_blocks]
                
                # Count visuals and checks
                has_svg = any(b.block_type == "suggested_diagram" and (b.content.get("svg_content") or b.content.get("svg")) for b in p_blocks)
                has_photo = any(b.block_type == "suggested_image" and (b.content.get("resolved_image_url") or b.content.get("url")) for b in p_blocks)
                has_check = any(b.block_type == "knowledge_check" for b in p_blocks)

                if has_svg: t_svgs += 1
                if has_photo: t_photos += 1
                if has_check: t_checks += 1

                visual_tag = "[SVG DIAGRAM]" if has_svg else ("[WIKIMEDIA PHOTO]" if has_photo else "")
                check_tag = "[KNOWLEDGE CHECK]" if has_check else ""
                tag = f"{visual_tag} {check_tag}".strip()

                print(f"  Page {p_num:02d}: {p_title[:42]:<42} | Blocks: {len(p_blocks)} ({', '.join(comp_types)}) {tag}")

        t_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
        grand_pages += t_pages
        grand_blocks += t_blocks
        grand_svgs += t_svgs
        grand_photos += t_photos
        grand_checks += t_checks
        grand_assets += t_assets

        print(f"\n>>> Topic {topic.order} Summary: {len(lessons)} Lessons | {t_pages} Pages | {t_blocks} Blocks | {t_svgs} SVGs | {t_photos} Photos | {t_assets} Assets")

    print("\n" + "=" * 80)
    print("FORM 4 GEOGRAPHY OVERALL CURRICULUM AUDIT SUMMARY")
    print("=" * 80)
    print(f"Total Topics:            {len(topics)}")
    print(f"Total Lessons:           {sum(t.lessons.count() for t in topics)}")
    print(f"Total Pages:             {grand_pages}")
    print(f"Total Lesson Blocks:     {grand_blocks}")
    print(f"Inline Vector SVGs:      {grand_svgs}")
    print(f"Wikimedia Photos:        {grand_photos}")
    print(f"Interactive Checkpoints: {grand_checks}")
    print(f"Total Media Assets:      {grand_assets}")
    print("=" * 80)

if __name__ == "__main__":
    audit_form4_geography()
