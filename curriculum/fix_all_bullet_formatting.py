"""
Database Migration & Normalization Script: Standardize All Bullet Lists to Markdown Lists (- )

Converts:
  - Unicode bullet markers ('•', '\u2022') at start of lines into '- '
  - Inline bullet markers separated by spaces into '\n- '
  - Ensures clean markdown list structure across all LessonBlock content fields.

Usage:
  ./venv/bin/python curriculum/fix_all_bullet_formatting.py
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def normalize_text_bullets(text: str) -> str:
    if not text or not isinstance(text, str):
        return text
    
    # 1. Convert lines starting with bullet character
    cleaned = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    
    # 2. Convert inline bullets separated by spaces or punctuation into new line list items
    cleaned = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', cleaned)
    
    # 3. Ensure a blank line before the first list item IF preceded by a regular paragraph line
    cleaned = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', cleaned, flags=re.MULTILINE)
    
    return cleaned

def normalize_content_recursive(data):
    if isinstance(data, str):
        return normalize_text_bullets(data)
    elif isinstance(data, dict):
        return {k: normalize_content_recursive(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [normalize_content_recursive(item) for item in data]
    return data

def run_bullet_normalization():
    print("=" * 80)
    print("STARTING BULLET NORMALIZATION ACROSS ALL LESSON BLOCKS")
    print("=" * 80)

    blocks = LessonBlock.objects.all()
    updated_count = 0

    with transaction.atomic():
        for b in blocks:
            old_content = b.content
            new_content = normalize_content_recursive(old_content)
            
            if old_content != new_content:
                b.content = new_content
                b.save(update_fields=["content"])
                updated_count += 1

    print(f"[SUCCESS] Checked {blocks.count()} LessonBlocks. Updated {updated_count} blocks with standardized Markdown lists.")
    print("=" * 80)

if __name__ == "__main__":
    run_bullet_normalization()
