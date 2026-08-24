import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson, Topic, LessonAsset

t = Topic.objects.get(id=81)
l = Lesson.objects.filter(topic=t).order_by('id').first()
b = LessonBlock.objects.filter(lesson=l, page_number=1, block_type='photo_view').first()

asset = LessonAsset.objects.filter(lesson=l, asset_type='photo').first()
if not asset:
    print("Asset missing! Creating...")
    img_data = {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Aerial_view_of_the_Nairobi_skyline_from_the_KICC_roof.jpg",
        "author": "Lebu Ayiga",
        "licensing": "CC BY-SA 4.0",
    }
    LessonAsset.objects.create(
        lesson=l,
        asset_type='photo',
        url=img_data['url'],
        metadata={
            'url': img_data['url'],
            'author': img_data['author'],
            'licensing': img_data['licensing']
        }
    )
    print("Asset created.")
else:
    print("Asset exists.")
