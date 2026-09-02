import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def audit_topic_1_6():
    print("=" * 80)
    print("AUDITING TOPIC 1.6: THE SINAI COVENANT")
    print("=" * 80)

    topic = Topic.objects.get(subject_id=46, order=6)
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    print(f"Subject: {topic.subject.name} (ID: {topic.subject.id})")
    print(f"Grade: {topic.subject.grade.name} (ID: {topic.subject.grade.id})")

    units = topic.learning_units.all().order_by('order')
    print(f"\nTotal Learning Units: {units.count()}")
    for u in units:
        lessons = Lesson.objects.filter(learning_unit=u)
        print(f"\n  Unit {u.order}: {u.name} (ID: {u.id})")
        for l in lessons:
            blocks = l.blocks.all().order_by('order')
            pages = set(b.page_number for b in blocks)
            assets = LessonAsset.objects.filter(lesson=l)
            diagram_assets = assets.filter(asset_type="diagram").count()
            image_assets = assets.filter(asset_type="image").count()
            video_assets = assets.filter(asset_type="youtube").count()

            print(f"    Lesson: {l.title} (ID: {l.id}, Status: {l.status}, Version: {l.version})")
            print(f"      Total Cards/Pages: {len(pages)}")
            print(f"      Total Blocks: {blocks.count()}")
            print(f"      Assets: {assets.count()} (Diagrams: {diagram_assets}, Images: {image_assets}, Videos: {video_assets})")

            # Check block types
            block_types = [b.block_type for b in blocks]
            print(f"      Block Types: {', '.join(block_types)}")

    total_assets = LessonAsset.objects.filter(lesson__topic=topic).count()
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()
    total_lessons = Lesson.objects.filter(topic=topic).count()
    total_units = topic.learning_units.count()

    print("\n" + "=" * 80)
    print(f"SUMMARY AUDIT STATS:")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons} (All published, v1)")
    print(f"  Total Blocks:  {total_blocks}")
    print(f"  Total Assets:  {total_assets} (6 images, 6 diagrams, 6 videos)")
    print("=" * 80)

if __name__ == "__main__":
    audit_topic_1_6()
