"""
VLearn Form 4 Biology — Curriculum Audit Engine

Audits all Form 4 Biology Topics, Lessons, Pages, Blocks, SVGs, Wikimedia photos, and LessonAssets.

Usage:
  ./venv/bin/python curriculum/audit_form4_biology.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def audit_form4_biology():
    print("=" * 80)
    print("VLEARN CURRICULUM AUDIT: FORM 4 BIOLOGY")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()

    if not subject:
        print("[!] Error: Form 4 Biology not found.")
        return

    topics = list(Topic.objects.filter(subject=subject).order_by("order"))
    print(f"[*] Found {len(topics)} Topics under Form 4 Biology (Subject ID: {subject.id}):\n")

    grand_lessons = 0
    grand_pages = 0
    grand_blocks = 0
    grand_svgs = 0
    grand_photos = 0
    grand_assets = 0
    grand_checkpoints = 0

    for t in topics:
        print("-" * 70)
        print(f"TOPIC {t.order}: {t.name} (ID: {t.id})")
        print("-" * 70)

        lessons = list(t.lessons.all().order_by("learning_unit__order"))
        t_pages = 0
        t_blocks = 0
        t_svgs = 0
        t_photos = 0
        t_assets = 0
        t_checkpoints = 0

        for l in lessons:
            l_blocks = list(l.blocks.all().order_by("order"))
            l_pages = set(b.page_number for b in l_blocks if b.page_number is not None)
            l_svg = sum(1 for b in l_blocks if b.block_type == "suggested_diagram" and (b.content.get("svg_content") or b.content.get("svg")))
            l_photo = sum(1 for b in l_blocks if b.block_type == "suggested_image" and (b.content.get("resolved_image_url") or b.content.get("url")))
            l_assets = LessonAsset.objects.filter(lesson=l).count()
            l_kc = sum(1 for b in l_blocks if b.block_type == "knowledge_check")

            t_pages += len(l_pages)
            t_blocks += len(l_blocks)
            t_svgs += l_svg
            t_photos += l_photo
            t_assets += l_assets
            t_checkpoints += l_kc

            print(f"  Lesson {l.learning_unit.order}: {l.title} (ID: {l.id})")
            print(f"    - Pages: {len(l_pages)} | Blocks: {len(l_blocks)} | SVGs: {l_svg} | Photos: {l_photo} | Assets: {l_assets} | KC: {l_kc}")

        print(f"\n>>> Topic {t.order} Totals: {len(lessons)} Lessons | {t_pages} Pages | {t_blocks} Blocks | {t_svgs} SVGs | {t_photos} Photos | {t_assets} Assets | {t_checkpoints} KC\n")

        grand_lessons += len(lessons)
        grand_pages += t_pages
        grand_blocks += t_blocks
        grand_svgs += t_svgs
        grand_photos += t_photos
        grand_assets += t_assets
        grand_checkpoints += t_checkpoints

    print("=" * 80)
    print("FORM 4 BIOLOGY OVERALL CURRICULUM AUDIT SUMMARY")
    print("=" * 80)
    print(f"Total Topics:            {len(topics)}")
    print(f"Total Lessons:           {grand_lessons}")
    print(f"Total Pages:             {grand_pages}")
    print(f"Total Lesson Blocks:     {grand_blocks}")
    print(f"Inline Vector SVGs:      {grand_svgs}")
    print(f"Wikimedia Photos:        {grand_photos}")
    print(f"Interactive Checkpoints: {grand_checkpoints}")
    print(f"Total Media Assets:      {grand_assets}")
    print("=" * 80)

if __name__ == "__main__":
    audit_form4_biology()
