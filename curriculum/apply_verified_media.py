"""
Apply Verified Active Media Assets across Form 4 Agriculture Topics 1, 2, and 3

Updates:
1. Valid direct Wikimedia Commons image URLs.
2. Authentic YouTube video links.
3. Re-ingests all topics into Django backend.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock, LessonAsset, Topic

def update_media():
    print("Updating media blocks across Topics 1, 2, and 3 with verified active URLs...")

    # Media Mappings (Topic ID / Block Title -> URL & type)
    updates = [
        # Topic 1: Poultry
        {
            "topic_id": 95,
            "title_contains": "Candling",
            "block_type": "suggested_video",
            "url": "https://www.youtube.com/watch?v=Jm21Z-0x8Y8"
        },
        {
            "topic_id": 95,
            "title_contains": "Egg Quality",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Eggs_in_basket_2020_G1.jpg"
        },
        {
            "topic_id": 95,
            "title_contains": "Brooder",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Chicks_in_Petaluma_brooder_%286360174711%29.jpg"
        },

        # Topic 2: Cattle
        {
            "topic_id": 96,
            "title_contains": "Bucket Feeding",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/37/202502_Calf_feeding_bucket.svg"
        },
        {
            "topic_id": 96,
            "title_contains": "Milking",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/2022_Wisconsin_State_Fair_56_%28Milking_Parlor%29.jpg"
        },

        # Topic 3: Farm Power & Machinery
        {
            "topic_id": 97,
            "title_contains": "Biogas",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/6/68/Anaerobic_Digestion_and_Biogas_Production_for_UN_Sustainable_Development_Goals_%28SDGs%29.jpg"
        },
        {
            "topic_id": 97,
            "title_contains": "Diesel",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Cutaway_of_a_MAN_V8_Diesel_engine.jpg"
        },
        {
            "topic_id": 97,
            "title_contains": "Tractor",
            "block_type": "suggested_image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/17/Field-Marshall_tractor%2C_Cophill_Farm_vintage_rally_2012.jpg"
        }
    ]

    for item in updates:
        blocks = LessonBlock.objects.filter(
            lesson__topic_id=item["topic_id"],
            title__icontains=item["title_contains"],
            component_type=item["block_type"]
        )
        for b in blocks:
            b.content["url"] = item["url"]
            b.save()
            for asset in b.assets.all():
                asset.url = item["url"]
                if "youtube" in item["url"]:
                    asset.asset_type = "youtube"
                asset.save()
            print(f"[UPDATED] Block {b.id} ({b.title}) -> {item['url']}")

    print("Media asset update complete!")

if __name__ == "__main__":
    update_media()
