import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
import django
django.setup()

from curriculum.models import Topic, Lesson, LessonAsset, LessonBlock

def apply_video_updates():
    with open('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/discovered_videos.json', 'r') as f:
        discovered = json.load(f)
        
    print(f"Applying {len(discovered)} verified YouTube video replacements...")
    
    updated_assets = 0
    updated_blocks = 0
    
    for key, data in discovered.items():
        topic_order, unit_order = map(int, key.split('_'))
        vid = data['video_id']
        title = data['title']
        author = data['author']
        
        lesson = Lesson.objects.filter(
            topic__subject_id=51,
            topic__order=topic_order,
            learning_unit__order=unit_order
        ).first()
        
        if not lesson:
            print(f"Warning: Lesson not found for T{topic_order}.L{unit_order}")
            continue
            
        # Update LessonAsset
        yt_assets = LessonAsset.objects.filter(lesson=lesson, asset_type='youtube')
        for asset in yt_assets:
            asset.title = title
            asset.url = f"https://www.youtube.com/watch?v={vid}"
            if not isinstance(asset.metadata, dict):
                asset.metadata = {}
            asset.metadata['youtube_id'] = vid
            asset.metadata['title'] = title
            asset.metadata['channel'] = author
            asset.status = 'attached'
            asset.save()
            updated_assets += 1
            
        # Update suggested_video LessonBlock
        video_blocks = LessonBlock.objects.filter(lesson=lesson, component_type='suggested_video')
        for block in video_blocks:
            c = block.content or {}
            c['youtube_id'] = vid
            c['title'] = title
            c['url'] = f"https://www.youtube.com/watch?v={vid}"
            c['channel'] = author
            block.content = c
            block.save()
            updated_blocks += 1
            
        print(f"  [UPDATED] T{topic_order}.L{unit_order} '{lesson.title}' -> {vid} ('{title}')")
        
    print(f"\nDone! Updated {updated_assets} LessonAsset records and {updated_blocks} LessonBlock records.")

if __name__ == '__main__':
    apply_video_updates()
