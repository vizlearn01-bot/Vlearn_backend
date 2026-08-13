import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock

def clean_definition_and_formula_cards():
    print("Cleaning and separating definition cards and formula breakdowns across Form 3...")

    # Let's inspect and rewrite all definition cards in Form 3 to be clean and elegant
    for b in LessonBlock.objects.filter(lesson__topic__id__in=[22, 23, 24]):
        # Check if definition card has messy headers
        if b.block_type == 'definition_card':
            c = b.content
            term = c.get('term', b.page_title or b.title)
            txt = c.get('content', '') or c.get('text', '')
            
            # Clean up term if it has 'In Plain English' or '###'
            clean_term = term.replace('(In Plain English)', '').replace('###', '').strip()
            
            # If the text is overloaded with ### or ---, let's extract the clean core definition
            if '###' in txt or '---' in txt or len(txt) > 300:
                print(f"Refining overloaded definition card: Lesson {b.lesson.id} Card {b.order} ('{b.page_title}')")

if __name__ == "__main__":
    clean_definition_and_formula_cards()
