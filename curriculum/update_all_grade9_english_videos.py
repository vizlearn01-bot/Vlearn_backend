"""
VLearn CBC Grade 9 English — Video Asset Updater Script
Applies verified live YouTube video IDs to all 30 lessons across Topics 1, 2, 3, and 4.
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from django.db import transaction
from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

VERIFIED_VIDEOS = {
    # Topic 1 (Lessons 1-8)
    (1, 1): {"id": "3C8qKxWYufQ", "title": "Polite English & Euphemisms Explained"},
    (1, 2): {"id": "7wUCyjiyXdg", "title": "Active & Empathetic Listening Skills"},
    (1, 3): {"id": "SoErQfLkqjY", "title": "The Secret to Winning Any Negotiation"},
    (1, 4): {"id": "uQEuo7woEEk", "title": "STAR Interview Questions and Answers Technique"},
    (1, 5): {"id": "SehA30-v-nM", "title": "Impromptu Speaking: Speaking on the Spot"},
    (1, 6): {"id": "Qsop8rmkw4s", "title": "Selective Listening & Note-Taking Techniques"},
    (1, 7): {"id": "lI3xTvwYsa8", "title": "Master English Pronunciation: The 8 Diphthong Vowel Sounds"},
    (1, 8): {"id": "0KZiB-XuTNU", "title": "Understand English Question Tags & Intonation"},

    # Topic 2 (Lessons 1-7)
    (2, 1): {"id": "X5yJRAOlA1U", "title": "Types of Reading: Scanning, Skimming, Intensive & Extensive"},
    (2, 2): {"id": "0bZGBInjEX8", "title": "Note Making, Visualising and Summarising (SQ4R)"},
    (2, 3): {"id": "ctVlFUNy0n4", "title": "Genres of Oral Literature: Tongue Twisters & Riddles"},
    (2, 4): {"id": "MPafjfmJh48", "title": "What is Rhyme Scheme: Definition, Types & Examples"},
    (2, 5): {"id": "uwmww8-DTy0", "title": "Drama Stage Directions & Play Structure"},
    (2, 6): {"id": "JT_NIFpY1WI", "title": "Direct Characterization vs. Indirect Characterization"},
    (2, 7): {"id": "cI6WYuGFALc", "title": "Analyzing Literature: Identifying Themes and Stylistic Patterns"},

    # Topic 3 (Lessons 1-8)
    (3, 1): {"id": "oix99eQ8sJI", "title": "Grade 9 English: Gender-Neutral and Inclusive Language"},
    (3, 2): {"id": "VVB8xRght-M", "title": "Countable vs. Uncountable Nouns & Quantifiers"},
    (3, 3): {"id": "tUfZjEXG5aQ", "title": "Relative Pronouns: Who, Whom, Whose, Which, That"},
    (3, 4): {"id": "clIMqTFLbNc", "title": "The Order of Adjectives & Adverb Comparison"},
    (3, 5): {"id": "JavBn2OlE8I", "title": "Complex Prepositions & Correlative Conjunctions"},
    (3, 6): {"id": "36wG9pSYu7Q", "title": "Modal Auxiliaries: Can, Could, May, Might, Must, Should"},
    (3, 7): {"id": "O9YRy8m1Rf8", "title": "All Perfect Tenses: Present Perfect and Past Perfect Aspects"},
    (3, 8): {"id": "aaYM3Wygc44", "title": "Complex Sentences and Reported / Indirect Speech"},

    # Topic 4 (Lessons 1-7)
    (4, 1): {"id": "gfYq2ng9s4E", "title": "English Punctuation Guide & Spelling Mechanics"},
    (4, 2): {"id": "p_jWfaMdh7A", "title": "How to Structure a Paragraph: Topic, Support & Clincher"},
    (4, 3): {"id": "Mo4ezba9EE8", "title": "Formal Letters & Application for Scholarship Guidelines"},
    (4, 4): {"id": "1XctnF7C74s", "title": "8 Professional Email Etiquette Tips"},
    (4, 5): {"id": "KGImUx4zg64", "title": "The 6-Stage Writing Process Pipeline"},
    (4, 6): {"id": "AXn4ABWe138", "title": "Narrative Composition & Story Plot Structure"},
    (4, 7): {"id": "mvF_i4YJwas", "title": "Common English Idioms & Figurative Meanings"}
}


def update_database_videos():
    grade = Grade.objects.get(id=18)
    subject = Subject.objects.get(grade=grade, name="English")
    print(f"[*] Updating videos for Grade 9 English (Subject ID: {subject.id})...")

    updated_count = 0
    with transaction.atomic():
        for (top_order, unit_order), vdata in VERIFIED_VIDEOS.items():
            topic = Topic.objects.filter(subject=subject, order=top_order).first()
            if not topic:
                print(f"[!] Topic {top_order} not found!")
                continue
            unit = LearningUnit.objects.filter(topic=topic, order=unit_order).first()
            if not unit:
                print(f"[!] Unit {unit_order} in Topic {top_order} not found!")
                continue
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            if not lesson:
                print(f"[!] Lesson in Unit {unit_order} not found!")
                continue

            yt_id = vdata["id"]
            yt_url = f"https://www.youtube.com/watch?v={yt_id}"
            yt_title = vdata["title"]

            # Update LessonAsset
            video_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube").first()
            if video_asset:
                video_asset.url = yt_url
                video_asset.title = yt_title
                video_asset.metadata = {"youtube_id": yt_id}
                video_asset.save()
            else:
                video_asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="youtube",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=yt_title,
                    description=f"Educational guide for {lesson.title}",
                    url=yt_url,
                    metadata={"youtube_id": yt_id}
                )

            # Update LessonBlock
            video_block = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_video").first()
            if video_block:
                content = video_block.content or {}
                content["youtube_id"] = yt_id
                content["url"] = yt_url
                content["title"] = yt_title
                video_block.content = content
                video_block.save()
                if not video_block.assets.filter(id=video_asset.id).exists():
                    video_block.assets.add(video_asset)

            updated_count += 1
            print(f"  [✔] Topic {top_order} Lesson {unit_order}: [{yt_id}] -> '{yt_title}'")

    print(f"\n[+] Successfully updated all {updated_count} video assets in the database!")


if __name__ == "__main__":
    update_database_videos()
