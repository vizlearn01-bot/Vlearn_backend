"""
VLearn CBC Grade 10 Agriculture — Universal Educational Video Injection Engine
Injects 100+ verified, active YouTube videos across all 17 Topics (>= 50% of lessons per topic).

Features:
  - 100% verified active YouTube URLs (pre-tested via YouTube oEmbed API)
  - Intelligently placed on Card 2 or Card 3 of relevant lessons
  - Creates/updates `suggested_video` LessonBlock and linked `LessonAsset` records
  - Fully atomic and idempotent

Usage:
  ./venv/bin/python curriculum/inject_verified_youtube_videos_all_topics.py
"""

import os
import sys
import json
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

@transaction.atomic
def inject_verified_youtube_videos():
    print("=" * 85)
    print("STARTING BULK EDUCATIONAL VIDEO INJECTION: CBC Grade 10 Agriculture (17 Topics)")
    print("=" * 85)

    curriculum = Curriculum.objects.get(name="CBC")
    grade = Grade.objects.get(curriculum=curriculum, name__icontains="10")
    subject = Subject.objects.get(grade=grade, name="Agriculture")

    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_verified_youtube_videos.json")
    with open(json_path, "r", encoding="utf-8") as f:
        video_db = json.load(f)

    total_videos_injected = 0
    topic_video_stats = {}

    for t_order_str, lessons_map in video_db.items():
        t_order = int(t_order_str)
        topic = Topic.objects.filter(subject=subject, order=t_order).first()
        if not topic:
            print(f"Warning: Topic order {t_order} not found!")
            continue

        print(f"\nProcessing Topic {t_order:2d}: {topic.name} ({len(lessons_map)} targeted videos)...")
        topic_injected = 0

        # Remove existing youtube assets for this topic so we don't accumulate duplicates
        LessonAsset.objects.filter(lesson__topic=topic, asset_type="youtube").delete()

        for u_order_str, v_data in lessons_map.items():
            u_order = int(u_order_str)
            lesson = Lesson.objects.filter(topic=topic, learning_unit__order=u_order).first()
            if not lesson:
                print(f"  [Unit {u_order:2d}] Lesson not found for Unit {u_order}!")
                continue

            v_url = v_data["url"]
            v_title = v_data["title"]
            v_author = v_data.get("author", "Educational Agriculture Channel")

            # Check if a suggested_video block already exists in this lesson
            video_block = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_video").first()

            if video_block:
                # Update existing video block
                video_block.title = f"Educational Video: {v_title}"
                video_block.content = {
                    "title": v_title,
                    "description": f"Field demonstration on '{v_data.get('query', topic.name)}' by {v_author}.",
                    "url": v_url,
                    "author": v_author,
                    "video_id": v_data.get("video_id")
                }
                video_block.save()
            else:
                # Target Page 2 or Page 3 for video demonstration
                all_blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
                pages = sorted(list(set(b.page_number for b in all_blocks)))
                
                # Pick page 2 if >= 3 pages, else page 2 or page 1
                target_page = 2 if len(pages) >= 2 else 1
                page_blocks = [b for b in all_blocks if b.page_number == target_page]
                target_comp_order = len(page_blocks) + 1

                video_block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g10_agri_t{t_order}_u{u_order}_p{target_page}_video",
                    block_type="suggested_video",
                    component_type="suggested_video",
                    title=f"Educational Video: {v_title}",
                    content={
                        "title": v_title,
                        "description": f"Field demonstration on '{v_data.get('query', topic.name)}' by {v_author}.",
                        "url": v_url,
                        "author": v_author,
                        "video_id": v_data.get("video_id")
                    },
                    order=len(all_blocks) + 1,
                    page_number=target_page,
                    component_order=target_comp_order,
                    metadata={"topic_order": t_order, "unit_order": u_order, "page": target_page}
                )

            # Link LessonAsset record
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Lesson {u_order} Video: {v_title}",
                description=f"Field video tutorial on '{v_data.get('query', topic.name)}' by {v_author}.",
                url=v_url,
                metadata={
                    "topic_order": t_order,
                    "unit_order": u_order,
                    "youtube_url": v_url,
                    "video_id": v_data.get("video_id"),
                    "author": v_author
                }
            )
            video_block.assets.add(asset)
            topic_injected += 1
            total_videos_injected += 1
            print(f"  [Video Attached] Unit {u_order:2d}: {v_title[:45]}... ({v_url})")

        topic_video_stats[t_order] = {
            "name": topic.name,
            "total_lessons": topic.lessons.count(),
            "videos_count": topic_injected,
            "percentage": round((topic_injected / topic.lessons.count()) * 100, 1)
        }

    print("\n" + "=" * 85)
    print(f"BULK VIDEO INJECTION COMPLETE: {total_videos_injected} Educational Videos Injected Across 17 Topics")
    print("=" * 85)
    print(f"{'Topic':<5} | {'Topic Name':<45} | {'Lessons':<8} | {'Videos':<7} | {'Coverage':<10}")
    print("-" * 85)
    for t_order, stat in topic_video_stats.items():
        print(f"{t_order:<5} | {stat['name']:<45} | {stat['total_lessons']:<8} | {stat['videos_count']:<7} | {stat['percentage']}%")
    print("=" * 85)

if __name__ == "__main__":
    inject_verified_youtube_videos()
