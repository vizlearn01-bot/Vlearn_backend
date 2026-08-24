"""
VLearn Universal Chemistry — Concept Headings Sanitization Engine
Replaces or cleans robotic headings (e.g., 'Concept 1:', 'Concept 2:', 'Concept:', 'Concept Explanation')
with clear, student-friendly, curriculum-accurate titles.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def clean_title(title, fallback=""):
    if not title:
        return title
    
    t = title.strip()
    
    # Specific replacements
    replacements = {
        "Concept Explanation": "Core Principles & Conceptual Foundations",
        "📝 Concept Practice Questions": "Practice Questions & Analysis",
        "📝 Concept Practice Question": "Practice Question & Analysis",
        "📝 Quick Concept Check": "Quick Understanding Check",
        "Misconception Buster: Check Your Understanding & Misconception Buster": "Common Misconceptions & Scientific Corrections",
        "Check Your Understanding & Misconception Buster": "Common Misconceptions & Scientific Corrections",
        "Diagram: Visualizing Nuclear Concepts": "Visual Breakdown & Theoretical Diagram",
        "What is a Salt? (The Conceptual Definition)": "Definition & Structure of Salts",
        "Metals in Nature & The Concept of Ores": "Metals in Nature & Occurrence of Ores",
        "The Conceptual Shift: Acceleration at Constant Speed": "Centripetal Acceleration at Constant Speed",
        "Electrode Potential Concept": "Electrochemical Electrode Potentials",
        "Understanding Check: Electrode Potential Concept": "Check Your Understanding: Electrode Potentials",
        "Introduction: The Concept of Half-Life": "Introduction to Radioactive Half-Life"
    }

    if t in replacements:
        return replacements[t]

    # Regex patterns
    t = re.sub(r'^(?:Core\s+|Key\s+)?Concept\s*\d*[:\s\-]+', '', t, flags=re.IGNORECASE)
    t = re.sub(r'^(?:Core\s+|Key\s+)?Concept[:\s\-]+', '', t, flags=re.IGNORECASE)
    t = re.sub(r'^Concept\b', 'Core Principle', t, flags=re.IGNORECASE)
    t = re.sub(r'\bThe Concept of\b', 'Understanding', t, flags=re.IGNORECASE)
    t = re.sub(r'\bConcept Practice\b', 'Practice', t, flags=re.IGNORECASE)

    return t.strip() or fallback

def sanitize_all_headings():
    print("=" * 80)
    print("SANITIZING ALL CONCEPT HEADINGS ACROSS CURRICULUM")
    print("=" * 80)

    blocks = LessonBlock.objects.all()
    cleaned_titles = 0
    cleaned_page_titles = 0

    for b in blocks:
        modified = False
        
        if b.title:
            new_title = clean_title(b.title, b.lesson.title if b.lesson else "")
            if new_title != b.title:
                b.title = new_title
                modified = True
                cleaned_titles += 1
                
        if b.page_title:
            new_pt = clean_title(b.page_title, b.lesson.title if b.lesson else "")
            if new_pt != b.page_title:
                b.page_title = new_pt
                modified = True
                cleaned_page_titles += 1

        if modified:
            b.save(update_fields=['title', 'page_title'])

    print(f"[*] Cleaned {cleaned_titles} block titles and {cleaned_page_titles} page titles.")
    print("=" * 80)
    print("ALL CONCEPT HEADINGS SUCCESSFULLY REPLACED WITH USER-FRIENDLY TITLES!")
    print("=" * 80)

if __name__ == "__main__":
    sanitize_all_headings()
