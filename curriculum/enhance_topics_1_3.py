import os, sys, django, re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson, Topic, Subject, LessonAsset
from curriculum.bs_verified_images import VERIFIED_IMAGES

IMAGE_MAPPING = {
    81: {
        1: 'nairobi_aerial',
        2: 'analyzing_financial_data',
        3: 'nairobi_aerial',
        4: 'kibera_slum',
        5: 'sgr_train',
        6: 'analyzing_financial_data',
        7: 'nairobi_aerial',
        8: 'central_bank_kenya',
    },
    83: {
        1: 'wangige_market',
        2: 'nairobi_vegetable',
        3: 'wangige_market',
        4: 'kibera_slum',
        5: 'jua_kali_fabricator',
        6: 'sgr_train',
    },
    82: {
        1: 'maasai_market',
        2: 'kenyan_currency',
        3: 'kenyan_currency',
        4: 'atm_machine',
        5: 'central_bank_kenya',
        6: 'bank_tellers',
        7: 'atm_machine',
        8: 'central_bank_kenya',
    }
}

topics = Topic.objects.filter(id__in=[81, 82, 83]).order_by('id')
lessons_added_image = 0
format_fixes = 0

for t in topics:
    lessons = Lesson.objects.filter(topic=t).order_by('id')
    for idx, lesson in enumerate(lessons):
        lesson_num = idx + 1
        img_key = IMAGE_MAPPING[t.id].get(lesson_num, 'nairobi_aerial')
        img_data = VERIFIED_IMAGES[img_key]
        
        # 1. ADD PHOTO VIEW BLOCK
        page1_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by('order')
        first_block = page1_blocks.first()
        if first_block and first_block.block_type not in ['suggested_image', 'photo_view']:
            # Shift order
            for b in page1_blocks:
                b.order = b.order + 1
                b.save(update_fields=['order'])
            
            # Create new block
            new_block = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=0,
                block_type='photo_view',
                title=None,
                content={
                    'url': img_data['url'],
                    'text': img_data['description'],
                    'author': img_data['author'],
                    'licensing': img_data['licensing'],
                    'commons_page_url': img_data['commons_page_url']
                }
            )
            
            # Create LessonAsset
            LessonAsset.objects.create(
                lesson=lesson,
                asset_type='photo',
                url=img_data['url'],
                metadata={
                    'url': img_data['url'],
                    'author': img_data['author'],
                    'licensing': img_data['licensing']
                }
            )
            lessons_added_image += 1
            print(f"Added {img_key} to {lesson.title}")

        # 2. ENHANCE BLOCKS (Bullet points, Learning Goals)
        all_blocks = LessonBlock.objects.filter(lesson=lesson)
        for b in all_blocks:
            changed = False
            
            def convert_bullets(text):
                if not isinstance(text, str): return text, False
                new_text = text
                if '•' in new_text:
                    new_text = re.sub(r'(?m)^[ \t]*•[ \t]*', '- ', new_text)
                    new_text = new_text.replace(' • ', '\n- ')
                    new_text = new_text.replace('• ', '- ')
                    new_text = new_text.replace('•', '- ')
                return new_text, new_text != text

            if b.block_type == 'learning_goal' and 'goals' not in b.content:
                text = b.content.get('text', '')
                if text:
                    bullets = []
                    lines = text.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line.startswith('-') or line.startswith('•'):
                            bullets.append(line.lstrip('-•').strip())
                    
                    if bullets:
                        b.content['goals'] = bullets
                    else:
                        cleaned_text = text.replace('By the end of this lesson, you will be able to:', '').replace('By the end of this lesson, you should be able to', '').strip()
                        b.content['goals'] = [cleaned_text]
                    
                    # Remove text to clean up
                    if 'text' in b.content:
                        del b.content['text']
                        
                    changed = True

            def process_dict(d):
                d_changed = False
                for k, v in list(d.items()):
                    if isinstance(v, str):
                        new_v, v_changed = convert_bullets(v)
                        if v_changed:
                            d[k] = new_v
                            d_changed = True
                    elif isinstance(v, list):
                        for i, item in enumerate(v):
                            if isinstance(item, str):
                                new_item, item_changed = convert_bullets(item)
                                if item_changed:
                                    v[i] = new_item
                                    d_changed = True
                            elif isinstance(item, dict):
                                if process_dict(item):
                                    d_changed = True
                    elif isinstance(v, dict):
                        if process_dict(v):
                            d_changed = True
                return d_changed

            if process_dict(b.content):
                changed = True
                
            if changed:
                b.save(update_fields=['content'])
                format_fixes += 1

print(f"\nDone! Lessons added image: {lessons_added_image}")
print(f"Blocks formatted: {format_fixes}")
